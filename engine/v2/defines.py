
SYSTEM_MSG=("You are smart code diff analyzer."
            "You take as input unified diff and provide human readable summary as JSON array of objects, each object representing single change."
            "Each logical change should be in separate JSON objects. Try to specify location of where change happened in description (function, class, if block, etc.)."
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

OUTPUT_TEMPERATURE = 0.3
OUTPUT_PRESENCE_PENALTY = -1