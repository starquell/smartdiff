
from dataclasses import dataclass


SYSTEM_MSG=("You are smart code diff analyzer."
            "You take as input unified diff and provide human readable summary as JSON array of objects, each object representing single change."
            "Divide different logical change into separate JSON objects. Try to specify location of where change happened in description (function, class, if block, etc.)."
            "Do not make big judgements about the code quality and consequences of change, just describe the change."
)

FUNCTION = {
    "type": "function",
    "function": {
        "name": "register_changes",
        "parameters": {
            "type": "object",
            "properties": {
                "changes": {
                    "type": "array",
                    "description": "Changes in the code",
                    "items": {
                        "type": "object",
                        "description": "Single change in the code",
                        "properties": {
                            "short": {
                                "type": "string",
                                "description": "Short description"
                            },
                            "long": {
                                "type": "string",
                                "description": "Longer description"
                            },
                            "code": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "before": {
                                            "type": "string",
                                            "description": "Code before the change"
                                        },
                                        "after": {
                                            "type": "string",
                                            "description": "Code after the change"
                                        }
                                    }
                                }
                            }
                        },
                        "required": ["short", "long", "code"]
                    }
                }
            }
        },
    }
}
UNIFIED_DIFF_CONTEXT_LINES = 3

@dataclass 
class ModelInfo:
    name: str
    usd_per_1m_input_tokens: float
    usd_per_1m_output_tokens: float


FINETUNED_MODEL = ModelInfo(name = "ft:gpt-3.5-turbo-0125:personal:smartdiff-alt-v1:9Igz2jaW", usd_per_1m_input_tokens=3., usd_per_1m_output_tokens=6.)
GPT3_5 = ModelInfo(name = "gpt3.5-turbo", usd_per_1m_input_tokens=0.5, usd_per_1m_output_tokens=1.5)
GPT4 = ModelInfo(name = "gpt-4-turbo", usd_per_1m_input_tokens=10, usd_per_1m_output_tokens=30)
MODEL = FINETUNED_MODEL

OUTPUT_TEMPERATURE = 0.3
OUTPUT_PRESENCE_PENALTY = -1