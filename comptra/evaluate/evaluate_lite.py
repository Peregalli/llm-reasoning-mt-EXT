#!/usr/bin/env python3
"""Lightweight evaluation script that computes BLEU and chrF++ scores without heavy models."""

import json
import argparse
import os
from pathlib import Path
from sacrebleu.metrics import BLEU, CHRF
from comptra.data.dataset import get_datasets

bleu = BLEU(tokenize="flores200")
chrf = CHRF(word_order=2)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--translation_file",
        type=str,
        required=True,
        help="Path to the translate_0.jsonl file containing predictions.",
    )
    parser.add_argument(
        "--dataset_name_or_path",
        type=str,
        default="flores",
        help="Name of the dataset (e.g., flores, ntrex, tico)",
    )
    parser.add_argument(
        "--src", type=str, required=True, help="Source language (e.g., English)"
    )
    parser.add_argument(
        "--tgt", type=str, required=True, help="Target language (e.g., French)"
    )
    parser.add_argument(
        "--number_of_predictions",
        type=int,
        default=None,
        help="Number of predictions to evaluate (default: all)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # Load reference dataset
    print(f"Loading {args.dataset_name_or_path} dataset...")
    ds_tgt = get_datasets(args.dataset_name_or_path, args.tgt)
    references = [example["sentence"] for example in ds_tgt["devtest"]]

    # Load predictions
    print(f"Loading predictions from {args.translation_file}...")
    predictions = []
    with open(args.translation_file, "r") as fin:
        for line in fin:
            data = json.loads(line)
            predictions.append(data["translation"])

    # Limit to specified number
    if args.number_of_predictions:
        predictions = predictions[: args.number_of_predictions]
        references = references[: args.number_of_predictions]

    print(f"Evaluating {len(predictions)} translations...")

    # Compute scores
    bleu_score = bleu.corpus_score(predictions, [references])
    chrf_score = chrf.corpus_score(predictions, [references])

    # Print results
    print("\n" + "=" * 60)
    print(f"Translation: {args.src} → {args.tgt}")
    print(f"Dataset: {args.dataset_name_or_path}")
    print(f"File: {args.translation_file}")
    print(f"Samples: {len(predictions)}")
    print("=" * 60)
    print(f"BLEU:   {bleu_score.score:.2f}")
    print(f"chrF++: {chrf_score.score:.2f}")
    print("=" * 60)


if __name__ == "__main__":
    main()