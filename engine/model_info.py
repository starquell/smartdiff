from dataclasses import dataclass


@dataclass 
class ModelInfo:
    name: str
    usd_per_1m_input_tokens: float
    usd_per_1m_output_tokens: float


FINETUNED_MODEL = ModelInfo(name = "ft:gpt-3.5-turbo-0125:personal:smartdiff-alt-v1:9Igz2jaW", usd_per_1m_input_tokens=3., usd_per_1m_output_tokens=6.)
GPT3_5 = ModelInfo(name = "gpt-3.5-turbo", usd_per_1m_input_tokens=0.5, usd_per_1m_output_tokens=1.5)
GPT4 = ModelInfo(name = "gpt-4-turbo", usd_per_1m_input_tokens=10, usd_per_1m_output_tokens=30)

MODEL_MAP = {
    FINETUNED_MODEL.name: FINETUNED_MODEL,
    GPT3_5.name: GPT3_5,
    GPT4.name: GPT4
}
