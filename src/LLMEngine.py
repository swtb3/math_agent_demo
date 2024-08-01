from copy import deepcopy
from enum import Enum
from typing import Dict, List
from transformers import (
    pipeline,
    AutoTokenizer
)
import torch
from warnings import warn

class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    TOOL_CALL = "tool-call"
    TOOL_RESPONSE = "tool-response"

    @classmethod
    def roles(cls):
        return [r.value for r in cls]


def get_clean_message_list(message_list: List[Dict[str, str]], role_conversions: Dict[str, str] = {}):
    """
    Subsequent messages with the same role will be concatenated to a single message.

    Args:
        message_list (`List[Dict[str, str]]`): List of chat messages.
    """
    final_message_list = []
    message_list = deepcopy(message_list)
    for message in message_list:
        if not set(message.keys()) == {"role", "content"}:
            raise ValueError("Message should contain only 'role' and 'content' keys!")

        role = message["role"]
        if role not in MessageRole.roles():
            raise ValueError(f"Incorrect role {role}, only {MessageRole.roles()} are supported for now.")

        if role in role_conversions:
            message["role"] = role_conversions[role]

        if len(final_message_list) > 0 and message["role"] == final_message_list[-1]["role"]:
            final_message_list[-1]["content"] += "\n=======\n" + message["content"]
        else:
            final_message_list.append(message)
    return final_message_list


llama_role_conversions = {
    MessageRole.TOOL_RESPONSE: MessageRole.USER,
}


class HfEngine:
    def __init__(self, model_id: str = "meta-llama/Meta-Llama-3.1-8B-Instruct", config: dict = None):
        try:
            self.gpu_available = torch.cuda.is_available()
            self.ampere_available = True if (torch.cuda.get_device_capability(0)[0] == 8) & (self.gpu_available) else False
        except Exception as e:
            message = f'{e} - defaulting to cpu inference'
            warn(message)
            self.gpu_available = False
            self.ampere_available = False
        self.model_id = model_id
        self.pipe = pipeline(
            task ="text-generation",
            model=model_id,
            tokenizer=AutoTokenizer.from_pretrained(model_id, token=config["API"]["HF_READ"]),
            model_kwargs={
                "torch_dtype": torch.float16,
                "low_cpu_mem_usage": True,
                "attn_implementation": "flash_attention_2" if self.ampere_available else None,
                "quantization_config": {
                    "load_in_4bit": True,
                    "bnb_4bit_use_double_quant": True,
                    "bnb_4bit_compute_dtype": torch.float16, #Ampere architecure could use bfloat16,
                    "bnb_4bit_quant_type": "nf4"
                } if self.gpu_available else None,
            },
            token=config["API"]["HF_READ"],
            device_map="auto" if self.gpu_available else "cpu",
            trust_remote_code=True
        )
        
    
    def __call__(self, messages: List[Dict[str, str]], stop_sequences=[]) -> str:
        
        messages = get_clean_message_list(messages, role_conversions=llama_role_conversions)
        outputs = self.pipe(messages, max_new_tokens=1500, stop_strings=stop_sequences, tokenizer=self.pipe.tokenizer)
        response = outputs[0]["generated_text"][-1]["content"]
        return str(response)