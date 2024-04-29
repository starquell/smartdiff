# Smartdiff

**LLM-powered semantic diff tool**



Usage: 
1. Put you OpenAI API token and model name in .env in cli/ directory like this:
```
OPENAI_API_KEY=sk-proj-my-token
MODEL=some-gpt-based-model
```

2. Install dependencies
```
   pip install -r /path/to/requirements.txt
```

3. Run!
```
python -m cli.main <original_file> <changed_file>
```
