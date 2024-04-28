from engine.v1.change import TextRange, SingleChange
from typing import List

def extract_snippet(file: str, snippet: TextRange) -> str:
    as_lines = file.splitlines()
    
    if snippet.first_line == snippet.last_line:
        # If the start and end are on the same line, extract part of this line
        return as_lines[snippet.first_line - 1][snippet.first_col - 1 : snippet.last_col]
    else:
        # Extract parts of the first and last lines
        first_part = as_lines[snippet.first_line - 1][snippet.first_col - 1 :]
        last_part = as_lines[snippet.last_line - 1][:snippet.last_col]
        
        # Extract complete lines if any between the first and last
        middle_part = as_lines[snippet.first_line : snippet.last_line - 1]
        
        # Combine all parts together
        return "\n".join([first_part] + middle_part + [last_part])

def visualize_changes(file_lhs: str, file_rhs: str, changes: List[SingleChange]):
    for change in changes:
        print("**************************")
        print(change.short_desc)
        print(change.long_desc)
        for location in change.locations:
            print("* Single change *")
            if location.removed:
                print("Removed: ")
                print(f"{extract_snippet(file_lhs, location.removed)}")
            if location.added:
                print("Added: ")
                print(f"{extract_snippet(file_rhs, location.added)}")
            print()
        print()