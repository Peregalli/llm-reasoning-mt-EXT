ARGS="
    --model_name_or_path google/metricx-24-hybrid-large-v2p6\
    --dataset_name_or_path flores\
    --max_input_length 256\
    --batch_size 1\
    --data_dir /home/onyxia/work/llm-reasoning-mt-EXT/predictions\
    --number_of_predictions 300\
    --seed 122\
    --num_workers 8\
    --metric metricx\
    --languages Xhosa\
    --strategies IOFT-qwen\
    --names checkpoint-200 checkpoint-2200\
"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

python -m comptra.evaluate.test $ARGS