import json

diffs_loc = "diffs"
jsons_loc = "outputV2"

TRAIN_RANGE = range(1, 31)
TEST_RANGE = range(31, 39)

SYSTEM_MSG=("You are smart code diff analyzer."
            "You take as input unified diff and provide human readable summary as JSON array of objects, each object representing single change."
            "Object should have fields: short (short description), long (long description), locations."
            "locations should be array of objects with fields: removed, added. Removed and added fields are optional, but it should be at least one of them. removed and added should be objects with fields: line, col, end_line, end_col."
            "Be very precise in calculating location (line, col, end_line, end_col) of changes. Divide different logical change into separate JSON objects."
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
                            "locations": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "removed": {
                                            "type": "object",
                                            "description": "Location of removed part of code in this change",
                                            "properties": {
                                                "line": {
                                                    "type": "integer",
                                                    "description": "First line of removed part"
                                                },
                                                "col": {
                                                    "type": "integer",
                                                    "description": "Column of first symbol of removed part"
                                                },
                                                "end_line": {
                                                    "type": "integer",
                                                    "description": "Last line of removed part"
                                                },
                                                "end_col": {
                                                    "type": "integer",
                                                    "description": "Column of first symbol of removed part"
                                                }
                                            }
                                        },
                                        "added": {
                                            "type": "object",
                                            "properties": {
                                                "line": {
                                                    "type": "integer",
                                                },
                                                "col": {
                                                    "type": "integer",
                                                },
                                                "end_line": {
                                                    "type": "integer",
                                                },
                                                "end_col": {
                                                    "type": "integer",
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "required": ["short", "long", "locations"]
                    }
                }
            }
        },
    }
}


FUNCTION_V2 = {
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



def generate_one_example(diff_path, json_path):
    input = open(diff_path, "r").read()
    output = open(json_path, "r").read()
    return json.dumps({
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_MSG
            },
            {
                "role": "user",
                "content": input
            },
            {
                "role": "assistant",
                "function_call": {
                    "name": FUNCTION_V2["function"]["name"],
                    "arguments": output
                }
            }
        ],
        "functions": [FUNCTION_V2["function"]]
    })


def generate_dataset_file(dataset_range, output_file):
    result = ""

    for i in dataset_range:
        diff_path = f"{diffs_loc}/{i}.md"
        json_path = f"{jsons_loc}/{i}.json"
        result += generate_one_example(diff_path, json_path)
        result += "\n"

    with open(output_file, "w") as f:
        f.write(result)

generate_dataset_file(TRAIN_RANGE, "fine_tuning_train.jsonl")
generate_dataset_file(TEST_RANGE, "fine_tuning_test.jsonl")