### Input command
```
python\
  evaluation.py\
  --model_name_or_path Qwen/Qwen2.5-0.5B\
  --tokenizer_name_or_path Qwen/Qwen2.5-0.5B\
  --src English\
  --tgt Xhosa\
  --request_batch_size 64\
  --inference_api vllm\
  --max_samples 10000\
  --num_return_sequences 1\
  --num_beams 1\
  --max_new_tokens 256\
  --temperature 0.0\
  --top_p 1.0\
  --repetition_penalty 1.0\
  --output_dir GENERATIONS/FLORES/QWEN-2.5-0.5B/VANILLA\
  --k 0\
  --seed 122\
  --method_divide llm\
  --merge_prompt vanilla\
  --method_translate vanilla\
  --selection_method greedy\
  --steps 0\
  --verbose\
  --number_of_subproblems 0\
  --number_of_refining_steps 0\
  --template_key 14\
  --retriever_type bm25s\
  --dataset_name_or_path flores
```
### Translations file
GENERATIONS/FLORES/QWEN-2.5-0.5B/VANILLA/Qwen2.5-0.5B/English_to_Xhosa_0_shot_seed_122_llm_vanilla_0_0_0/translate_0.jsonl

### Eval command
````
python -m comptra.evaluate.test \
  --data_dir GENERATIONS/FLORES/QWEN-2.5-0.5B \
  --dataset_name_or_path flores \
  --metric metricx \
  --model_name_or_path google/metricx-23-large-v2p0 \
  --number_of_predictions 1012 \
  --languages Xhosa \
  --strategies VANILLA \
  --names Qwen2.5-0.5B
````

### Results

BLEU = 1.4087040866385876
chrF++ = 7.788722585181407
metricx = 20.365709146492094


### Input command

```
python\
  evaluation.py\
  --model_name_or_path Qwen/Qwen2.5-3B\
  --tokenizer_name_or_path Qwen/Qwen2.5-3B\
  --src English\
  --tgt Xhosa\
  --request_batch_size 64\
  --inference_api vllm\
  --max_samples 10000\
  --num_return_sequences 1\
  --num_beams 1\
  --max_new_tokens 256\
  --temperature 0.0\
  --top_p 1.0\
  --repetition_penalty 1.0\
  --output_dir GENERATIONS/FLORES/QWEN-2.5-3B/VANILLA\
  --k 0\
  --seed 122\
  --method_divide llm\
  --merge_prompt vanilla\
  --method_translate vanilla\
  --selection_method greedy\
  --steps 0\
  --verbose\
  --number_of_subproblems 0\
  --number_of_refining_steps 0\
  --template_key 14\
  --retriever_type bm25s\
  --dataset_name_or_path flores
```

### Translations file
GENERATIONS/FLORES/QWEN-2.5-3B/VANILLA/Qwen2.5-3B/English_to_Xhosa_0_shot_seed_122_llm_vanilla_0_0_0/translate_0.jsonl

### Eval command
````
python -m comptra.evaluate.test \
  --data_dir GENERATIONS/FLORES/QWEN-2.5-3B \
  --dataset_name_or_path flores \
  --metric metricx \
  --model_name_or_path google/metricx-23-large-v2p0 \
  --number_of_predictions 1012 \
  --languages Xhosa \
  --strategies VANILLA \
  --names Qwen2.5-3B
```

### Results

BLEU = 0.27713872970343467
chrF++ = 5.821347125641728
metricx = 21.96116137598814

### Input command
`
python\
  evaluation.py\
  --model_name_or_path Qwen/Qwen2.5-1.5B\
  --tokenizer_name_or_path Qwen/Qwen2.5-1.5B\
  --src English\
  --tgt Xhosa\
  --request_batch_size 64\
  --inference_api vllm\
  --max_samples 10000\
  --num_return_sequences 1\
  --num_beams 1\
  --max_new_tokens 256\
  --temperature 0.0\
  --top_p 1.0\
  --repetition_penalty 1.0\
  --output_dir GENERATIONS/FLORES/QWEN-2.5-1.5B/VANILLA\
  --k 0\
  --seed 122\
  --method_divide llm\
  --merge_prompt vanilla\
  --method_translate vanilla\
  --selection_method greedy\
  --steps 0\
  --verbose\
  --number_of_subproblems 0\
  --number_of_refining_steps 0\
  --template_key 14\
  --retriever_type bm25s\
  --dataset_name_or_path flores
`

### Translations file

GENERATIONS/FLORES/QWEN-2.5-1.5B/VANILLA/Qwen2.5-1.5B/English_to_Xhosa_0_shot_seed_122_llm_vanilla_0_0_0/translate_0.jsonl

### Eval command

python -m comptra.evaluate.test \
  --data_dir GENERATIONS/FLORES/QWEN-2.5-1.5B \
  --dataset_name_or_path flores \
  --metric metricx \
  --model_name_or_path google/metricx-23-large-v2p0 \
  --number_of_predictions 1012 \
  --languages Xhosa \
  --strategies VANILLA \
  --names Qwen2.5-1.5B


### Results

BLEU = 0.6274674307979741
chrF++ = 7.2025989760090265
metricx = 22.37135622529644

### Input command

python\
  evaluation.py\
  --model_name_or_path Qwen/Qwen2.5-3B\
  --tokenizer_name_or_path Qwen/Qwen2.5-3B\
  --src English\
  --tgt Xhosa\
  --request_batch_size 64\
  --inference_api vllm\
  --max_samples 10000\
  --num_return_sequences 1\
  --num_beams 1\
  --max_new_tokens 256\
  --temperature 0.0\
  --top_p 1.0\
  --repetition_penalty 1.0\
  --output_dir GENERATIONS/FLORES/QWEN-2.5-3B/VANILLA\
  --k 0\
  --seed 122\
  --method_divide llm\
  --merge_prompt vanilla\
  --method_translate vanilla\
  --selection_method greedy\
  --steps 0\
  --verbose\
  --number_of_subproblems 0\
  --number_of_refining_steps 0\
  --template_key 14\
  --retriever_type bm25s\
  --dataset_name_or_path flores

### Translations file

GENERATIONS/FLORES/QWEN-2.5-3B/VANILLA/Qwen2.5-3B/English_to_Xhosa_0_shot_seed_122_llm_vanilla_0_0_0/translate_0.jsonl

### Eval command

python -m comptra.evaluate.test \
  --data_dir GENERATIONS/FLORES/QWEN-2.5-3B \
  --dataset_name_or_path flores \
  --metric metricx \
  --model_name_or_path google/metricx-23-large-v2p0 \
  --number_of_predictions 1012 \
  --languages Xhosa \
  --strategies VANILLA \
  --names Qwen2.5-3B

### Results

BLEU = 0.27971024194611877
chrF++ = 5.830485746543686
metricx = 21.99309072381423
### Results Curve

```python
import matplotlib.pyplot as plt

# Model names and their corresponding metricx scores
models = [
  "Qwen2.5-0.5B",
  "Qwen2.5-1.5B",
  "Qwen2.5-3B"
]
metricx_scores = [
  20.37,  # Qwen2.5-0.5B
  22.37,  # Qwen2.5-1.5B
  21.99   # Qwen2.5-3B
]

plt.figure(figsize=(7, 4))
plt.plot(models, metricx_scores, marker='o', linestyle='-', color='b')
plt.title("MetricX Scores for Qwen2.5 Models (English→Xhosa, VANILLA)")
plt.xlabel("Model")
plt.ylabel("MetricX Score")
plt.ylim(min(metricx_scores) - 1, max(metricx_scores) + 1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
```

Copy and run this Python code to visualize the MetricX scores for the different Qwen2.5 model sizes.

### Input command

```
ARGS="\
    --model_name_or_path  /teamspace/studios/this_studio/llm-reasoning-mt-EXT-agustina/checkpoints-gemma-3-1b-xho-ext-sp/checkpoint-2000\
    --tokenizer_name_or_path google/gemma-3-1b-pt\
    --base_model_name_or_path google/gemma-3-1b-pt\
    --src English\
    --tgt Xhosa\
    --request_batch_size 256\
    --inference_api vllm\
    --max_samples 256\
    --num_return_sequences 1\
    --num_beams 1\
    --temperature 0.0\
    --top_p 1.0\
    --repetition_penalty 1.0\
    --output_dir predictions/IOFT-gemma/\
    --seed 42\
    --method_divide identity\
    --merge_prompt vanilla\
    --method_translate vanilla\
    --selection_method greedy\
    --steps 0\
    --verbose\
    --number_of_subproblems 0\
    --template_key 14\
    --retriever_type bm25s\
    --dataset_name_or_path flores\
    --number_of_merge_demonstrations 0\
    --nllb_name_or_path /teamspace/studios/this_studio/llm-reasoning-mt-EXT-agustina/checkpoints-gemma-3-1b-xho-ext-sp/checkpoint-2000\
    --enable_lora\
    --lora_rank 32\
    "
python evaluation.py $ARGS  
```

### Translations file
llm-reasoning-mt-EXT-agustina/predictions/IOFT-gemma/checkpoint-2000/English_to_Xhosa_None_shot_seed_42_identity_vanilla_0_0_0/translate_0.jsonl

### Eval command
```
python -m comptra.evaluate.test \
  --data_dir /teamspace/studios/this_studio/llm-reasoning-mt-EXT-agustina/predictions/ \
  --dataset_name_or_path flores \
  --metric metricx \
  --model_name_or_path google/metricx-23-large-v2p0 \
  --number_of_predictions 256 \
  --languages Xhosa \
  --strategies IOFT-gemma \
  --names checkpoint-2000 \
```

### Results
BLEU = 7.19489043320587
chrF++ = 23.18462607496555
metricx = 15.9769287109375