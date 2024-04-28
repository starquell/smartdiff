import json
from typing import List

from engine.v2.change import SingleChange

def parse_single_change(change_json: dict) -> SingleChange:
    short_desc = change_json["short"]
    long_desc = change_json["long"]
    code_changes = []
    for location in change_json["code"]:
        before = location.get("before")
        after = location.get("after")
        code_changes.append(SingleChange.CodeChange(before=before, after=after))
    return SingleChange(short_desc=short_desc, long_desc=long_desc, code_changes=code_changes)


def parse_changes(model_output: str) -> List[SingleChange]:
    object = json.loads(model_output)
    return [parse_single_change(change) for change in object["changes"]]
