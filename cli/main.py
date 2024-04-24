import sys
import os

from dotenv import load_dotenv
from engine import DiffEngine

load_dotenv()

print(os.getcwd())

def read_file_or_exit(path: str) -> str:
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
        exit(1)
    except Exception as e:
        print(f"Error reading file {path}: {e}")
        exit(1) 

if len(sys.argv) < 3:
    print("Usage: python main.py file1.txt file2.txt")

file_lhs = read_file_or_exit(sys.argv[1])
file_rhs = read_file_or_exit(sys.argv[2])

engine = DiffEngine(open_ai_api_key_env='OPENAI_API_KEY')
diff = engine.get_diff(file_lhs, file_rhs)
print(diff)
