
SYSTEM_MSG=None

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
