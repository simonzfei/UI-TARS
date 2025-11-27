
```bash
(agent) f@f:$ python -m vllm.entrypoints.openai.api_server --served-model-name ui-tars --model /weights/checkpoints/UI-TARS -tp 1 --max-model-len 8192
INFO 04-02 21:41:05 api_server.py:712] vLLM API server version 0.6.6
INFO 04-02 21:41:05 api_server.py:713] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/weights/checkpoints/UI-TARS', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=8192, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=None, enable_prefix_caching=None, disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=0, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.9, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_seqs=None, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_overrides=None, enforce_eager=False, max_seq_len_to_capture=8192, disable_custom_all_reduce=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt=None, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_speculative_tokens=None, speculative_disable_mqa_scorer=False, speculative_draft_tensor_parallel_size=None, speculative_max_model_len=None, speculative_disable_by_batch_size=None, ngram_prompt_lookup_max=None, ngram_prompt_lookup_min=None, spec_decoding_acceptance_method='rejection_sampler', typical_acceptance_sampler_posterior_threshold=None, typical_acceptance_sampler_posterior_alpha=None, disable_logprobs_during_spec_decoding=None, model_loader_extra_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=['ui-tars'], qlora_adapter_name_or_path=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', generation_config=None, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False)
INFO 04-02 21:41:05 api_server.py:199] Started engine process with PID 8122
INFO 04-02 21:41:08 config.py:510] This model supports multiple tasks: {'reward', 'generate', 'embed', 'score', 'classify'}. Defaulting to 'generate'.
INFO 04-02 21:41:10 config.py:510] This model supports multiple tasks: {'score', 'classify', 'embed', 'generate', 'reward'}. Defaulting to 'generate'.
INFO 04-02 21:41:10 llm_engine.py:234] Initializing an LLM engine (v0.6.6) with config: model='/weights/checkpoints/UI-TARS', speculative_config=None, tokenizer='/weights/checkpoints/UI-TARS', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=ui-tars, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output"],"candidate_compile_sizes":[],"compile_sizes":[],"capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=True, 
INFO 04-02 21:41:11 selector.py:120] Using Flash Attention backend.
INFO 04-02 21:41:11 model_runner.py:1094] Starting to load model weights/checkpoints/UI-TARS...
WARNING 04-02 21:41:11 utils.py:624] Current `vllm-flash-attn` has a bug inside vision module, so we use xformers backend instead. You can run `pip install flash-attn` to use flash-attention backend.
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:33<01:40, 33.49s/it]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [01:03<01:03, 31.72s/it]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [01:33<00:30, 30.93s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [01:47<00:00, 24.04s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [01:47<00:00, 26.86s/it]

INFO 04-02 21:42:59 model_runner.py:1099] Loading model weights took 15.5083 GB
Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
INFO 04-02 21:43:03 worker.py:241] Memory profiling takes 4.42 seconds
INFO 04-02 21:43:03 worker.py:241] the current vLLM instance can use total_gpu_memory (23.67GiB) x gpu_memory_utilization (0.90) = 21.30GiB
INFO 04-02 21:43:03 worker.py:241] model weights take 15.51GiB; non_torch_memory takes 0.28GiB; PyTorch activation peak memory takes 1.16GiB; the rest of the memory reserved for KV Cache is 4.36GiB.
INFO 04-02 21:43:03 gpu_executor.py:76] # GPU blocks: 5102, # CPU blocks: 4681
INFO 04-02 21:43:03 gpu_executor.py:80] Maximum concurrency for 8192 tokens per request: 9.96x
INFO 04-02 21:43:05 model_runner.py:1415] Capturing cudagraphs for decoding. This may lead to unexpected consequences if the model is not static. To run the model in eager mode, set 'enforce_eager=True' or use '--enforce-eager' in the CLI. If out-of-memory error occurs during cudagraph capture, consider decreasing `gpu_memory_utilization` or switching to eager mode. You can also reduce the `max_num_seqs` as needed to decrease memory usage.
Capturing CUDA graph shapes: 100%|████████████████████████████████████| 35/35 [00:08<00:00,  4.00it/s]
INFO 04-02 21:43:14 model_runner.py:1535] Graph capturing finished in 9 secs, took 1.92 GiB
INFO 04-02 21:43:14 llm_engine.py:431] init engine (profile, create kv cache, warmup model) took 14.74 seconds
INFO 04-02 21:43:14 api_server.py:640] Using supplied chat template:
INFO 04-02 21:43:14 api_server.py:640] None
INFO 04-02 21:43:14 launcher.py:19] Available routes are:
INFO 04-02 21:43:14 launcher.py:27] Route: /openapi.json, Methods: HEAD, GET
INFO 04-02 21:43:14 launcher.py:27] Route: /docs, Methods: HEAD, GET
INFO 04-02 21:43:14 launcher.py:27] Route: /docs/oauth2-redirect, Methods: HEAD, GET
INFO 04-02 21:43:14 launcher.py:27] Route: /redoc, Methods: HEAD, GET
INFO 04-02 21:43:14 launcher.py:27] Route: /health, Methods: GET
INFO 04-02 21:43:14 launcher.py:27] Route: /tokenize, Methods: POST
INFO 04-02 21:43:14 launcher.py:27] Route: /detokenize, Methods: POST
INFO 04-02 21:43:14 launcher.py:27] Route: /v1/models, Methods: GET
INFO 04-02 21:43:14 launcher.py:27] Route: /version, Methods: GET
INFO 04-02 21:43:14 launcher.py:27] Route: /v1/chat/completions, Methods: POST
INFO 04-02 21:43:14 launcher.py:27] Route: /v1/completions, Methods: POST
INFO 04-02 21:43:14 launcher.py:27] Route: /v1/embeddings, Methods: POST
INFO 04-02 21:43:14 launcher.py:27] Route: /pooling, Methods: POST
INFO 04-02 21:43:14 launcher.py:27] Route: /score, Methods: POST
INFO 04-02 21:43:14 launcher.py:27] Route: /v1/score, Methods: POST
INFO:     Started server process [8097]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)



INFO 04-02 22:32:10 logger.py:37] Received request chatcmpl-13fda6e307de4e7eacfb056888205c04: prompt: 'User: <|vision_start|><|image_pad|><|vision_end|>\nYou are a GUI agent. You are given a task and your action history, with screenshots. You need to perform the next action to complete the task. \n\n## Output Format\n\n\n## Action Space\n\nclick(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\nleft_double(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\nright_single(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\ndrag(start_box=\'<|box_start|>(x1,y1)<|box_end|>\', end_box=\'<|box_start|>(x3,y3)<|box_end|>\')\nhotkey(key=\'\')\ntype(content=\'\') #If you want to submit your input, use "\\" at the end of `content`.\nscroll(start_box=\'<|box_start|>(x1,y1)<|box_end|>\', direction=\'down or up or right or left\')\nwait() #Sleep for 5s and take a screenshot to check for any changes.\nfinished()\ncall_user() # Submit the task and call the user when the task is unsolvable, or when you need the user\'s help.\n\n## Note\n- Use Chinese in `Thought` part.\n- Summarize your next action (with its target element) in one sentence in `Thought` part.\n\n## User Instruction\n打开google浏览器，并打开页面中间的pytorch图片链接\n\nThought: 鼠标左键单击桌面左侧位置的“Google Chrome”图标，以打开浏览器。该图标是圆形的，外圈由红色、黄色和绿色组成，内圈是一个蓝色的圆形。\nAction: click(start_box=\'(20,370)\')<|im_end|>\nAssistant: ', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=1.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=128, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None.
INFO 04-02 22:32:10 engine.py:267] Added request chatcmpl-13fda6e307de4e7eacfb056888205c04.
INFO 04-02 22:32:11 metrics.py:467] Avg prompt throughput: 616.5 tokens/s, Avg generation throughput: 6.8 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 3.7%, CPU KV cache usage: 0.0%.
INFO:     127.0.0.1:33024 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO 04-02 22:32:16 logger.py:37] Received request chatcmpl-7b74af4578054172afb8927f51b96305: prompt: 'User: <|vision_start|><|image_pad|><|vision_end|>\nYou are a GUI agent. You are given a task and your action history, with screenshots. You need to perform the next action to complete the task. \n\n## Output Format\n\n\n## Action Space\n\nclick(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\nleft_double(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\nright_single(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\ndrag(start_box=\'<|box_start|>(x1,y1)<|box_end|>\', end_box=\'<|box_start|>(x3,y3)<|box_end|>\')\nhotkey(key=\'\')\ntype(content=\'\') #If you want to submit your input, use "\\" at the end of `content`.\nscroll(start_box=\'<|box_start|>(x1,y1)<|box_end|>\', direction=\'down or up or right or left\')\nwait() #Sleep for 5s and take a screenshot to check for any changes.\nfinished()\ncall_user() # Submit the task and call the user when the task is unsolvable, or when you need the user\'s help.\n\n## Note\n- Use Chinese in `Thought` part.\n- Summarize your next action (with its target element) in one sentence in `Thought` part.\n\n## User Instruction\n打开google浏览器，并打开页面中间的pytorch图片链接\n\nThought: 鼠标左键单击桌面左侧位置的“Google Chrome”图标，以打开浏览器。该图标是圆形的，外圈由红色、黄色和绿色组成，内圈是一个蓝色的圆形。\nAction: click(start_box=\'(20,370)\')\n从屏幕截图可以看出，我已经打开了浏览器，所以这个步骤我选择直接点击点击了页面中间的“PyTorch”图标。\nAction: click(start_box=\'(671,501)\')<|im_end|>\nAssistant: ', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=1.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=128, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None.
INFO 04-02 22:32:16 engine.py:267] Added request chatcmpl-7b74af4578054172afb8927f51b96305.
INFO 04-02 22:32:17 metrics.py:467] Avg prompt throughput: 506.4 tokens/s, Avg generation throughput: 7.8 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 3.7%, CPU KV cache usage: 0.0%.
INFO:     127.0.0.1:33024 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO 04-02 22:32:22 logger.py:37] Received request chatcmpl-f76f07e6aa424fdb9ad24314b3be9405: prompt: 'User: <|vision_start|><|image_pad|><|vision_end|>\nYou are a GUI agent. You are given a task and your action history, with screenshots. You need to perform the next action to complete the task. \n\n## Output Format\n\n\n## Action Space\n\nclick(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\nleft_double(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\nright_single(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\ndrag(start_box=\'<|box_start|>(x1,y1)<|box_end|>\', end_box=\'<|box_start|>(x3,y3)<|box_end|>\')\nhotkey(key=\'\')\ntype(content=\'\') #If you want to submit your input, use "\\" at the end of `content`.\nscroll(start_box=\'<|box_start|>(x1,y1)<|box_end|>\', direction=\'down or up or right or left\')\nwait() #Sleep for 5s and take a screenshot to check for any changes.\nfinished()\ncall_user() # Submit the task and call the user when the task is unsolvable, or when you need the user\'s help.\n\n## Note\n- Use Chinese in `Thought` part.\n- Summarize your next action (with its target element) in one sentence in `Thought` part.\n\n## User Instruction\n打开google浏览器，并打开页面中间的pytorch图片链接\n\nThought: 鼠标左键单击桌面左侧位置的“Google Chrome”图标，以打开浏览器。该图标是圆形的，外圈由红色、黄色和绿色组成，内圈是一个蓝色的圆形。\nAction: click(start_box=\'(20,370)\')\n从屏幕截图可以看出，我已经打开了浏览器，所以这个步骤我选择直接点击点击了页面中间的“PyTorch”图标。\nAction: click(start_box=\'(671,501)\')\n从屏幕截图可以看出，我已经打开了浏览器，已经被电脑选中，所以我不需要进行点击就可以继续完成任务选择。\nAction: click(start_box=\'(671,501)\')<|im_end|>\nAssistant: ', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=1.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=128, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None.
INFO 04-02 22:32:22 engine.py:267] Added request chatcmpl-f76f07e6aa424fdb9ad24314b3be9405.
INFO 04-02 22:32:23 metrics.py:467] Avg prompt throughput: 522.3 tokens/s, Avg generation throughput: 6.9 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 3.8%, CPU KV cache usage: 0.0%.
INFO:     127.0.0.1:33024 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO 04-02 22:32:34 metrics.py:467] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 2.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%.
INFO 04-02 22:32:44 metrics.py:467] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%.
INFO 04-02 22:33:17 logger.py:37] Received request chatcmpl-6e0600d4cf394a34b4ace0847a9940e5: prompt: 'User: <|vision_start|><|image_pad|><|vision_end|>\nYou are a GUI agent. You are given a task and your action history, with screenshots. You need to perform the next action to complete the task. \n\n## Output Format\n\n\n## Action Space\n\nclick(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\nleft_double(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\nright_single(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\ndrag(start_box=\'<|box_start|>(x1,y1)<|box_end|>\', end_box=\'<|box_start|>(x3,y3)<|box_end|>\')\nhotkey(key=\'\')\ntype(content=\'\') #If you want to submit your input, use "\\" at the end of `content`.\nscroll(start_box=\'<|box_start|>(x1,y1)<|box_end|>\', direction=\'down or up or right or left\')\nwait() #Sleep for 5s and take a screenshot to check for any changes.\nfinished()\ncall_user() # Submit the task and call the user when the task is unsolvable, or when you need the user\'s help.\n\n## Note\n- Use Chinese in `Thought` part.\n- Summarize your next action (with its target element) in one sentence in `Thought` part.\n\n## User Instruction\n打开google浏览器，并点击Microsoft Bing logo<|im_end|>\nAssistant: ', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=1.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=128, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None.
INFO 04-02 22:33:17 engine.py:267] Added request chatcmpl-6e0600d4cf394a34b4ace0847a9940e5.
INFO 04-02 22:33:19 metrics.py:467] Avg prompt throughput: 587.3 tokens/s, Avg generation throughput: 6.8 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 3.7%, CPU KV cache usage: 0.0%.
INFO:     127.0.0.1:51748 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO 04-02 22:33:24 logger.py:37] Received request chatcmpl-bf67157f5d9246cc8861fbf522562000: prompt: 'User: <|vision_start|><|image_pad|><|vision_end|>\nYou are a GUI agent. You are given a task and your action history, with screenshots. You need to perform the next action to complete the task. \n\n## Output Format\n\n\n## Action Space\n\nclick(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\nleft_double(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\nright_single(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\ndrag(start_box=\'<|box_start|>(x1,y1)<|box_end|>\', end_box=\'<|box_start|>(x3,y3)<|box_end|>\')\nhotkey(key=\'\')\ntype(content=\'\') #If you want to submit your input, use "\\" at the end of `content`.\nscroll(start_box=\'<|box_start|>(x1,y1)<|box_end|>\', direction=\'down or up or right or left\')\nwait() #Sleep for 5s and take a screenshot to check for any changes.\nfinished()\ncall_user() # Submit the task and call the user when the task is unsolvable, or when you need the user\'s help.\n\n## Note\n- Use Chinese in `Thought` part.\n- Summarize your next action (with its target element) in one sentence in `Thought` part.\n\n## User Instruction\n打开google浏览器，并点击Microsoft Bing logo\n\nThought: 根据任务要求，我需要打开google浏览器，并点击Microsoft Bing logo。在当前屏幕上，我可以清楚地看到左侧我已经打开了Visual Studio Code，在之前的操作中我错误的在相邻文本中间输入了“and”应该直接将鼠标移动到该文本z上双击选中该文本。\nAction: left_double(start_box=\'(209,445)\')<|im_end|>\nAssistant: ', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=1.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=128, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None.
INFO 04-02 22:33:24 engine.py:267] Added request chatcmpl-bf67157f5d9246cc8861fbf522562000.
INFO 04-02 22:33:25 metrics.py:467] Avg prompt throughput: 508.2 tokens/s, Avg generation throughput: 8.9 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 3.7%, CPU KV cache usage: 0.0%.
INFO:     127.0.0.1:51748 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO 04-02 22:33:28 logger.py:37] Received request chatcmpl-93258de7a5774798a2ebdd2b1b1aa86c: prompt: 'User: <|vision_start|><|image_pad|><|vision_end|>\nYou are a GUI agent. You are given a task and your action history, with screenshots. You need to perform the next action to complete the task. \n\n## Output Format\n\n\n## Action Space\n\nclick(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\nleft_double(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\nright_single(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\ndrag(start_box=\'<|box_start|>(x1,y1)<|box_end|>\', end_box=\'<|box_start|>(x3,y3)<|box_end|>\')\nhotkey(key=\'\')\ntype(content=\'\') #If you want to submit your input, use "\\" at the end of `content`.\nscroll(start_box=\'<|box_start|>(x1,y1)<|box_end|>\', direction=\'down or up or right or left\')\nwait() #Sleep for 5s and take a screenshot to check for any changes.\nfinished()\ncall_user() # Submit the task and call the user when the task is unsolvable, or when you need the user\'s help.\n\n## Note\n- Use Chinese in `Thought` part.\n- Summarize your next action (with its target element) in one sentence in `Thought` part.\n\n## User Instruction\n打开google浏览器，并点击Microsoft Bing logo\n\nThought: 根据任务要求，我需要打开google浏览器，并点击Microsoft Bing logo。在当前屏幕上，我可以清楚地看到左侧我已经打开了Visual Studio Code，在之前的操作中我错误的在相邻文本中间输入了“and”应该直接将鼠标移动到该文本z上双击选中该文本。\nAction: left_double(start_box=\'(209,445)\')\n为了打开google浏览器，并点击Microsoft Bing logo，我应该在键盘上按下Ctrl + Alt + T快捷键打开终端页面。\nAction: hotkey(key=\'ctrl   alt   t\')<|im_end|>\nAssistant: ', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=1.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=128, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None.
INFO 04-02 22:33:28 engine.py:267] Added request chatcmpl-93258de7a5774798a2ebdd2b1b1aa86c.
INFO 04-02 22:33:30 metrics.py:467] Avg prompt throughput: 612.5 tokens/s, Avg generation throughput: 14.6 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 3.8%, CPU KV cache usage: 0.0%.
INFO:     127.0.0.1:51748 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO 04-02 22:33:32 logger.py:37] Received request chatcmpl-a28402bd8af14b01b62544aa54911d5c: prompt: 'User: <|vision_start|><|image_pad|><|vision_end|>\nYou are a GUI agent. You are given a task and your action history, with screenshots. You need to perform the next action to complete the task. \n\n## Output Format\n\n\n## Action Space\n\nclick(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\nleft_double(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\nright_single(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\ndrag(start_box=\'<|box_start|>(x1,y1)<|box_end|>\', end_box=\'<|box_start|>(x3,y3)<|box_end|>\')\nhotkey(key=\'\')\ntype(content=\'\') #If you want to submit your input, use "\\" at the end of `content`.\nscroll(start_box=\'<|box_start|>(x1,y1)<|box_end|>\', direction=\'down or up or right or left\')\nwait() #Sleep for 5s and take a screenshot to check for any changes.\nfinished()\ncall_user() # Submit the task and call the user when the task is unsolvable, or when you need the user\'s help.\n\n## Note\n- Use Chinese in `Thought` part.\n- Summarize your next action (with its target element) in one sentence in `Thought` part.\n\n## User Instruction\n打开google浏览器，并点击Microsoft Bing logo\n\nThought: 根据任务要求，我需要打开google浏览器，并点击Microsoft Bing logo。在当前屏幕上，我可以清楚地看到左侧我已经打开了Visual Studio Code，在之前的操作中我错误的在相邻文本中间输入了“and”应该直接将鼠标移动到该文本z上双击选中该文本。\nAction: left_double(start_box=\'(209,445)\')\n为了打开google浏览器，并点击Microsoft Bing logo，我应该在键盘上按下Ctrl + Alt + T快捷键打开终端页面。\nAction: hotkey(key=\'ctrl   alt   t\')\n为了打开google浏览器，并点击Microsoft Bing logo，我应该在键盘上按下Ctrl + Alt + T快捷键打开终端页面。\nAction: hotkey(key=\'ctrl alt t\')<|im_end|>\nAssistant: ', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=1.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=128, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None.
INFO 04-02 22:33:32 engine.py:267] Added request chatcmpl-a28402bd8af14b01b62544aa54911d5c.
INFO:     127.0.0.1:51748 - "POST /v1/chat/completions HTTP/1.1" 200 OK

INFO 04-02 22:33:36 logger.py:37] Received request chatcmpl-635188a9c36c4d4ab8b3fd375b39f2b9: 
prompt: 'User: <|vision_start|><|image_pad|><|vision_end|>\nYou are a GUI agent. You are given a task and your action history, with screenshots. You need to perform the next action to complete the task. \n\n## Output Format\n\n\n## 
Action Space\n\nclick(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\nleft_double(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\nright_single(start_box=\'<|box_start|>(x1,y1)<|box_end|>\')\ndrag(start_box=\'<|box_start|>(x1,y1)<|box_end|>\', end_box=\'<|box_start|>(x3,y3)<|box_end|>\')\nhotkey(key=\'\')\ntype(content=\'\') 
#If you want to submit your input, use "\\" at the end of `content`.\nscroll(start_box=\'<|box_start|>(x1,y1)<|box_end|>\', direction=\'down or up or right or left\')\nwait() #Sleep for 5s and take a screenshot to check for any changes.\nfinished()\ncall_user() # Submit the task and call the user when the task is unsolvable, or when you need the user\'s help.\n\n## Note\n- Use Chinese in `Thought` part.\n- Summarize your next action (with its target element) in one sentence in `
Thought` part.\n\n## User Instruction\n打开google浏览器，并点击Microsoft Bing logo\n\nThought: 根据任务要求，我需要打开google浏览器，并点击Microsoft Bing logo。在当前屏幕上，我可以清楚地看到左侧我已经打开了Visual Studio Code，在之前的操作中我错误的在相邻文本中间输入了“and”应该直接将鼠标移动到该文本z上双击选中该文本。\nAction: left_double(start_box=\'(209,445)\')\n为了打开google浏览器，并点击Microsoft Bing logo，我应该在键盘上按下Ctrl + Alt + T快捷键打开终端页面。\nAction: hotkey(key=\'ctrl   alt   t\')\n为了打开google浏览器，并点击Microsoft Bing logo，我应该在键盘上按下Ctrl + Alt + T快捷键打开终端页面。\nAction: hotkey(key=\'ctrl alt t\')\n为了打开google浏览器，并点击Microsoft Bing logo，我应该键入"ro.collab.wso2.com的方式来访问。"\nAction: type(content=\'ro(collab.wso2.com\')<|im_end|>\nAssistant: ', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=1.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=128, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None.
INFO 04-02 22:33:36 engine.py:267] Added request chatcmpl-635188a9c36c4d4ab8b3fd375b39f2b9.
INFO 04-02 22:33:38 metrics.py:467] Avg prompt throughput: 791.2 tokens/s, Avg generation throughput: 5.7 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 3.9%, CPU KV cache usage: 0.0%.
INFO:     127.0.0.1:51748 - "POST /v1/chat/completions HTTP/1.1" 200 OK


# client

(agent) f@f:/media/f/E/project/agentic/UI-TARS$ git push 
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 20 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.92 KiB | 1.92 MiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/simonzfei/UI-TARS.git
   d3b2cfc..d98b743  main -> main
(agent) f@f:/media/f/E/project/agentic/UI-TARS$ /home/f/anaconda3/envs/agent/bin/python /media/f/E/project/agentic/UI-TARS/auto.py
Iteration 0: Capturing screen...
Sending image and instructions to model...
Response from model:
Thought: 我已经成功打开Visual Studio
Code应用程序，但是我无法使用软件打开浏览器。
因此我需要左键单击左侧任务栏的“Google Chrome”，以方便进行操作。

Action: click(start_box='(22,375)')
Executing action: click at (22, 375)
Iteration 1: Capturing screen...
Sending image and instructions to model...
Response from model:
Thought: 由于软件打开过的网页之后会直接记录在历史记录中。
因此我无法将浏览器网址栏放大重新输入，现在我已经打开了Visual Studio Code应用程序，
因此我应该左键单击左侧任务栏的“Google Chrome”，以方便进行操作。

Action: click(start_box='(19,369)')
Executing action: click at (19, 369)
Iteration 2: Capturing screen...
Sending image and instructions to model...
Response from model:
任务真实无法完成，因此我目前将直接提交任务内容。

Action: finished()
Received finished() command. Exiting loop.
Agent loop finished.
(agent) f@f:/media/f/E/project/agentic/UI-TARS$ /home/f/anaconda3/envs/agent/bin/python /media/f/E/project/agentic/UI-TARS/auto.py
Iteration 0: Capturing screen...
Sending image and instructions to model...
Response from model:
Thought: 鼠标左键单击桌面左侧位置的“Google Chrome”图标，以打开浏览器。该图标是圆形的，外圈由红色、黄色和绿色组成，内圈是一个蓝色的圆形。
Action: click(start_box='(20,370)')
Executing action: click at (20, 370)
Iteration 1: Capturing screen...
Sending image and instructions to model...
Response from model:
从屏幕截图可以看出，我已经打开了浏览器，所以这个步骤我选择直接点击点击了页面中间的“PyTorch”图标。
Action: click(start_box='(671,501)')
Executing action: click at (671, 501)
Iteration 2: Capturing screen...
Sending image and instructions to model...
Response from model:
从屏幕截图可以看出，我已经打开了浏览器，已经被电脑选中，所以我不需要进行点击就可以继续完成任务选择。
Action: click(start_box='(671,501)')
Executing action: click at (671, 501)
Iteration 3: Capturing screen...
Sending image and instructions to model...
Response from model:
任务已完成，完成打开google浏览器，并打开页面中间的pytorch图片链接。
Action: finished()
Received finished() command. Exiting loop.
Agent loop finished.



(agent) f@f:/media/f/E/project/agentic/UI-TARS$ /home/f/anaconda3/envs/agent/bin/python /media/f/E/project/agentic/UI-TARS/auto.py
Iteration 0: Capturing screen...
Sending image and instructions to model...
Response from model:
Thought: 根据任务要求，我需要打开google浏览器，并点击Microsoft Bing logo。在当前屏幕上，我可以清楚地看到左侧我已经打开了Visual Studio Code，在之前的操作中我错误的在相邻文本中间输入了“and”应该直接将鼠标移动到该文本z上双击选中该文本。
Action: left_double(start_box='(209,445)')
Executing action: left_double at (209, 445)
Iteration 1: Capturing screen...
Sending image and instructions to model...
Response from model:
为了打开google浏览器，并点击Microsoft Bing logo，我应该在键盘上按下Ctrl + Alt + T快捷键打开终端页面。
Action: hotkey(key='ctrl   alt   t')
No valid action found in response. Skipping execution this iteration.
Iteration 2: Capturing screen...
Sending image and instructions to model...
Response from model:
为了打开google浏览器，并点击Microsoft Bing logo，我应该在键盘上按下Ctrl + Alt + T快捷键打开终端页面。
Action: hotkey(key='ctrl alt t')
No valid action found in response. Skipping execution this iteration.
Iteration 3: Capturing screen...
Sending image and instructions to model...
Response from model:
为了打开google浏览器，并点击Microsoft Bing logo，我应该键入"ro.collab.wso2.com的方式来访问。"
Action: type(content='ro(collab.wso2.com')
No valid action found in response. Skipping execution this iteration.
Iteration 4: Capturing screen...
Sending image and instructions to model...
Response from model:
 call_user() # 任务无法完成，需要用户辅助重新输入文字。
Action: call_user()
Received call_user() command. Exiting loop.
Agent loop finished.

```