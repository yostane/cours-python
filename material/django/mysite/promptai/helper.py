from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

step = 0


def ask_model(query: str) -> str:
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")
    new_user_input_ids = tokenizer.encode(
        f"{query}{tokenizer.eos_token}", return_tensors="pt"
    )
    bot_input_ids = (
        torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
        if step > 0
        else new_user_input_ids
    )
    chat_history_ids = model.generate(
        bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1] :][0],
        skip_special_tokens=True,
    )
    return response
