python -m comptra.evaluate.test \
  --data_dir GENERATIONS/FLORES/Qwen2.5-0.5B \
  --dataset_name_or_path flores \
  --metric metricx \
  --model_name_or_path google/metricx-23-large-v2p0 \
  --number_of_predictions 1012 \
  --languages French \
  --strategies MAPS \
  --names Qwen2.5-0.5B