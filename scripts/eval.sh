ARGS="\
    --model_name_or_path  /home/onyxia/work/llm-reasoning-mt-EXT/checkpoints-gemma-3-1b-xho/checkpoint-5000\
    --tokenizer_name_or_path google/gemma-3-1b-pt\
    --base_model_name_or_path google/gemma-3-1b-pt\
    --src English\
    --tgt Xhosa\
    --request_batch_size 4\
    --inference_api vllm\
    --max_samples 10000\
    --num_return_sequences 1\
    --num_beams 1\
    --max_new_tokens 2768\
    --temperature 0.0\
    --top_p 1.0\
    --repetition_penalty 1.0\
    --output_dir predictions/IOFT-gemma/\
    --seed 42\
    --method_divide identity\
    --merge_prompt vanilla\
    --method_translate vanilla\
    --selection_method greedy\
    --steps 1\
    --verbose\
    --number_of_subproblems 1\
    --template_key 14\
    --retriever_type bm25s\
    --dataset_name_or_path flores\
    --number_of_merge_demonstrations 0\
    --nllb_name_or_path ./checkpoints-gemma-3-1b-xho/checkpoint-5000\
    --enable_lora\
    --lora_rank 32\
    "
python evaluation.py $ARGS  
## python evaluation.py   #--model_name_or_path ./checkpoints-gemma-3-1b-xho/checkpoint-200   --base_model_name_or_path google/gemma-3-1b-pt   --tokenizer_name_or_path google/gemma-3-1b-pt   --src English   --tgt Xhosa   --dataset_name_or_path flores   --enable_lora   --inference_api vllm   --method_divide identity   --number_of_subproblems 1   --steps 1   --method_translate vanilla   --temperature 0.0   --top_p 1.0   --repetition_penalty 1.0   --merge_prompt vanilla   --selection_method greedy   --output_dir ./outputs   --max_samples 5 --lora_rank 32  --verbose