#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: bash scripts/eval_multiple_checkpoints.sh 800 1000 2000 4000"
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

for ckpt in "$@"; do
  if ! [[ "${ckpt}" =~ ^[0-9]+$ ]]; then
    echo "Error: checkpoint '${ckpt}' is not a valid number."
    exit 1
  fi

  MODEL_CKPT_PATH="./checkpoints-qwen25-15-xho/checkpoint-${ckpt}"
  NLLB_CKPT_PATH="./checkpoints-qwen25-15-xho/checkpoint-${ckpt}"

  echo "============================================================"
  echo "Running evaluation for checkpoint-${ckpt}"
  echo "model_name_or_path: ${MODEL_CKPT_PATH}"
  echo "nllb_name_or_path:  ${NLLB_CKPT_PATH}"
  echo "============================================================"

  python evaluation.py \
    --model_name_or_path "${MODEL_CKPT_PATH}" \
    --tokenizer_name_or_path Qwen/Qwen2.5-1.5B \
    --base_model_name_or_path Qwen/Qwen2.5-1.5B \
    --src English \
    --tgt Xhosa \
    --request_batch_size 64 \
    --inference_api vllm \
    --max_samples 300 \
    --num_return_sequences 1 \
    --num_beams 1 \
    --max_new_tokens 2768\
    --temperature 0.0 \
    --top_p 1.0 \
    --k 0\
    --repetition_penalty 1.0 \
    --output_dir predictions/IOFT-qwen_24-15/ \
    --seed 42 \
    --method_divide llm \
    --merge_prompt vanilla \
    --method_translate vanilla \
    --selection_method greedy \
    --steps 0 \
    --verbose \
    --number_of_subproblems 0 \
    --number_of_refining_steps 0\
    --template_key 14 \
    --retriever_type bm25s \
    --dataset_name_or_path flores \
    --number_of_merge_demonstrations 0 \
    --nllb_name_or_path "${NLLB_CKPT_PATH}" \
    --enable_lora \
    --lora_rank 32

done

echo "All requested checkpoint evaluations finished successfully."
