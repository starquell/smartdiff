import os
from openai import OpenAI
from difflib import unified_diff


UNIFIED_DIFF_CONTEXT_LINES = 3
MODEL="gpt-3.5-turbo"
SYSTEM_MSG=""

class DiffEngine:
    def __init__(self, open_ai_api_key_env: str):
        try:
            self.api_key = os.environ[open_ai_api_key_env]
        except KeyError:
            print(f"Environment variable {open_ai_api_key_env} not set")
            raise
        
        self.open_ai_client = OpenAI(api_key=self.api_key)
    
    def get_diff(self, before: str, after: str) -> str:
        unified = "\n".join(unified_diff(before.splitlines(), after.splitlines(), n=UNIFIED_DIFF_CONTEXT_LINES, lineterm=""))
        completion = self.open_ai_client.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_MSG},
                {"role": "user", "content": unified}
            ]
        )
        print(completion.choices[0].message)

    