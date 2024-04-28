import json
from typing import List

from engine.v1.change import SingleChange, TextRange

def parse_single_change(change_json: dict) -> SingleChange:
    short_desc = change_json["short"]
    long_desc = change_json["long"]
    locations = []
    for location in change_json["locations"]:

        removed = location.get("removed")
        if removed:
            removed = TextRange(
                first_line=removed["line"],
                first_col=removed["col"],
                last_line=removed["end_line"],
                last_col=removed["end_col"]
            )
            
        added = location.get("added")
        if added:
            added = TextRange(
                first_line=added["line"],
                first_col=added["col"],
                last_line=added["end_line"],
                last_col=added["end_col"]
            )
        locations.append(SingleChange.Location(removed=removed, added=added))
            
    return SingleChange(short_desc=short_desc, long_desc=long_desc, locations=locations)

def parse_changes_list(changes: List[dict]) -> List[SingleChange]:
    return [parse_single_change(change) for change in changes]

def parse_changes(model_output: str) -> List[SingleChange]:
    object = json.loads(model_output)
    return parse_changes_list(object["changes"])
