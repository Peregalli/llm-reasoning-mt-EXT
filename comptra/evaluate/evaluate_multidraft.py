#!/usr/bin/env python3
"""Prepare and evaluate multidraft outputs against inline references."""

import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np
from datasets import Dataset
from sacrebleu.metrics import BLEU, CHRF


bleu = BLEU(tokenize="flores200")
chrf = CHRF(word_order=2)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_file",
        type=str,
        required=True,
        help="Path to the multidraft jsonl file.",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        required=True,
        help="Directory where prepared evaluation files will be written.",
    )
    parser.add_argument(
        "--source_field",
        type=str,
        default="sentence",
        help="Field containing the source sentence.",
    )
    parser.add_argument(
        "--reference_field",
        type=str,
        default="translation",
        help="Field containing the reference translation.",
    )
    parser.add_argument(
        "--prediction_field",
        type=str,
        default="final_translation",
        help="Field containing the prediction to evaluate.",
    )
    parser.add_argument(
        "--skip_empty",
        action="store_true",
        help="Skip examples whose prediction is empty.",
    )
    parser.add_argument(
        "--metricx_model_name_or_path",
        type=str,
        default=None,
        help="Optional MetricX model path/name. If provided, MetricX will be computed.",
    )
    parser.add_argument(
        "--max_input_length",
        type=int,
        default=256,
        help="Maximum input length for MetricX.",
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        default=8,
        help="Batch size for MetricX.",
    )
    return parser.parse_args()


def _ensure_metricx23_importable() -> None:
    try:
        import metricx23  # noqa: F401
        return
    except ModuleNotFoundError:
        pass

    repo_root = Path(__file__).resolve().parents[2]
    candidate_paths = [
        repo_root / "metricx",
        repo_root / "third_party" / "metricx",
    ]

    for candidate in candidate_paths:
        if (candidate / "metricx23").is_dir():
            sys.path.insert(0, str(candidate))
            try:
                import metricx23  # noqa: F401
                return
            except ModuleNotFoundError:
                continue

    raise ModuleNotFoundError(
        "No module named 'metricx23'. Clone MetricX to "
        f"{repo_root / 'metricx'} or {repo_root / 'third_party' / 'metricx'}, "
        "or set PYTHONPATH to the MetricX repository root."
    )


def load_examples(args):
    examples = []
    with open(args.input_file, "r", encoding="utf-8") as fin:
        for line_number, line in enumerate(fin, start=1):
            data = json.loads(line)
            source = str(data.get(args.source_field, "")).strip()
            reference = str(data.get(args.reference_field, "")).strip()
            prediction = str(data.get(args.prediction_field, "")).strip()

            if args.skip_empty and not prediction:
                continue

            if not source or not reference:
                raise ValueError(
                    f"Missing source/reference at line {line_number} in {args.input_file}"
                )

            examples.append(
                {
                    "source": source,
                    "reference": reference,
                    "translation": prediction,
                }
            )
    return examples


def write_outputs(examples, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    pairs_path = os.path.join(output_dir, "pairs.jsonl")
    translate_path = os.path.join(output_dir, "translate_0.jsonl")
    metricx_path = os.path.join(output_dir, "metricx_input.jsonl")

    with open(pairs_path, "w", encoding="utf-8") as pairs_out, open(
        translate_path, "w", encoding="utf-8"
    ) as translate_out, open(metricx_path, "w", encoding="utf-8") as metricx_out:
        for example in examples:
            pairs_out.write(json.dumps(example, ensure_ascii=False) + "\n")
            translate_out.write(
                json.dumps(
                    {"translation": example["translation"]},
                    ensure_ascii=False,
                )
                + "\n"
            )
            metricx_out.write(
                json.dumps(
                    {
                        "source": example["source"],
                        "hypothesis": example["translation"],
                        "reference": example["reference"],
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )

    return pairs_path, translate_path, metricx_path


def compute_bleu_chrf(examples):
    predictions = [example["translation"] for example in examples]
    references = [example["reference"] for example in examples]
    bleu_score = bleu.corpus_score(predictions, [references]).score
    chrf_score = chrf.corpus_score(predictions, [references]).score
    return bleu_score, chrf_score


def compute_metricx(examples, args):
    import torch
    import transformers

    _ensure_metricx23_importable()
    from metricx23.models import MT5ForRegression

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    tokenizer = transformers.AutoTokenizer.from_pretrained("google/mt5-xl")

    try:
        model = MT5ForRegression.from_pretrained(
            args.metricx_model_name_or_path,
            dtype=torch.bfloat16,
        )
    except TypeError:
        model = MT5ForRegression.from_pretrained(
            args.metricx_model_name_or_path,
            torch_dtype=torch.bfloat16,
        )

    model.config.use_cache = False
    model.to(device)
    model.eval()

    per_device_batch_size = args.batch_size
    if torch.cuda.is_available():
        per_device_batch_size = max(1, args.batch_size // torch.cuda.device_count())

    training_args = transformers.TrainingArguments(
        output_dir=args.output_dir,
        per_device_eval_batch_size=per_device_batch_size,
        dataloader_pin_memory=False,
        report_to="none",
    )
    data_collator = transformers.DataCollatorWithPadding(
        tokenizer=tokenizer,
        padding="longest",
    )
    trainer = transformers.Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
    )

    def _make_input(example):
        example["input"] = (
            "candidate: "
            + example["hypothesis"]
            + " reference: "
            + example["reference"]
        )
        return example

    def _tokenize_metricx(example):
        tokenized = tokenizer(
            example["input"],
            max_length=args.max_input_length,
            truncation=True,
            padding=False,
        )
        input_ids = tokenized["input_ids"]
        attention_mask = tokenized.get("attention_mask", [1] * len(input_ids))

        if len(input_ids) > 1 and input_ids[-1] == tokenizer.eos_token_id:
            input_ids = input_ids[:-1]

        seq_len = min(len(input_ids), len(attention_mask))
        input_ids = input_ids[:seq_len]
        attention_mask = attention_mask[:seq_len]

        if seq_len == 0:
            pad_token_id = tokenizer.pad_token_id
            if pad_token_id is None:
                pad_token_id = tokenizer.eos_token_id
            input_ids = [pad_token_id]
            attention_mask = [0]

        tokenized["input_ids"] = input_ids
        tokenized["attention_mask"] = attention_mask
        return tokenized

    ds = Dataset.from_dict(
        {
            "source": [example["source"] for example in examples],
            "hypothesis": [example["translation"] for example in examples],
            "reference": [example["reference"] for example in examples],
        }
    )
    ds = ds.map(_make_input, load_from_cache_file=False)
    ds = ds.map(_tokenize_metricx, load_from_cache_file=False)
    ds = ds.remove_columns(
        [column for column in ds.column_names if column not in ["input_ids", "attention_mask"]]
    )
    score_predictions, _, _ = trainer.predict(test_dataset=ds)
    return float(np.mean([float(pred) for pred in score_predictions]))


def main():
    args = parse_args()
    examples = load_examples(args)

    if not examples:
        raise ValueError("No examples found to evaluate.")

    pairs_path, translate_path, metricx_path = write_outputs(examples, args.output_dir)
    bleu_score, chrf_score = compute_bleu_chrf(examples)

    print("=" * 60)
    print(f"Input file: {args.input_file}")
    print(f"Examples:   {len(examples)}")
    print(f"Pairs file: {pairs_path}")
    print(f"Pred file:  {translate_path}")
    print(f"MetricX in: {metricx_path}")
    print("=" * 60)
    print(f"BLEU:   {bleu_score:.2f}")
    print(f"chrF++: {chrf_score:.2f}")

    if args.metricx_model_name_or_path:
        metricx_score = compute_metricx(examples, args)
        print(f"MetricX: {metricx_score:.2f}")

    print("=" * 60)


if __name__ == "__main__":
    main()
