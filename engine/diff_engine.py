import os
import itertools

from typing import List
from difflib import unified_diff

from openai import OpenAI
from loguru import logger

from engine.v2.change import SingleChange
from engine.v2.output_parser import parse_changes
import engine.v2.defines as defines

class DiffEngine:
    def __init__(self, open_ai_api_key_env: str):
        try:
            self.api_key = os.environ[open_ai_api_key_env]
        except KeyError:
            print(f"Environment variable {open_ai_api_key_env} not set")
            raise
        
        self.open_ai_client = OpenAI(api_key=self.api_key)

    
    def get_diff(self, before: str, after: str) -> List[SingleChange]:
        unified = unified_diff(before.splitlines(), after.splitlines(), n=defines.UNIFIED_DIFF_CONTEXT_LINES, lineterm="")
        unified = itertools.islice(unified, 2, None)  ## Skipping the first two lines of the unified diff (--- and +++)
        unified = "\n".join(unified)

        logger.debug(f"Unified diff:\n{unified}\n\n")

        messages = [
            {"role": "system", "content": defines.SYSTEM_MSG},
            {"role": "user", "content": f"{unified}"}
        ]
        logger.debug("Sending request to OpenAI API...")
        completion = self.open_ai_client.chat.completions.create(
            model=defines.MODEL.name,
            messages=messages,
            tools=[defines.FUNCTION],
            temperature=defines.OUTPUT_TEMPERATURE,
            presence_penalty=defines.OUTPUT_PRESENCE_PENALTY,
        )
        logger.debug("Request completed")
        used_input_tokens = completion.usage.prompt_tokens if completion.usage else 0
        used_output_tokens = completion.usage.completion_tokens if completion.usage else 0
        logger.debug(f"Usage: {used_input_tokens} input tokens (~ {used_input_tokens / 1_000_000 * defines.MODEL.usd_per_1m_input_tokens} USD),"
                     f"{used_output_tokens} input tokens (~ {used_output_tokens / 1_000_000 * defines.MODEL.usd_per_1m_output_tokens} USD)")

        choice = completion.choices[0]

        if choice.finish_reason == "length":
            raise ValueError("API call failed: max tokens exceeded")

        logger.debug(f"Api response: {choice.message}\n\n")

        if not choice.message.tool_calls:
            raise ValueError("No tool calls in response");
        
        for call in choice.message.tool_calls:
            if call.function.arguments:
                return parse_changes(call.function.arguments)

        raise ValueError("Function calls with arguments not found")
        

    