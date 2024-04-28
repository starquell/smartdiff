from engine.v2.change import SingleChange
from typing import List
import textwrap

from tabulate import tabulate

MAX_LINE_LENGTH = 100


def format_diff_table(lhs: str, rhs: str) -> str:
    return tabulate([[lhs if lhs else "", rhs if rhs else ""]], headers=['before', 'after'], tablefmt='presto')

def visualize_changes(changes: List[SingleChange]) -> str:

    results = []

    for change in changes:
        table = [
            ["Change", "\n".join(textwrap.wrap(change.short_desc, width=MAX_LINE_LENGTH))],
            ["Description", "\n".join(textwrap.wrap(change.long_desc, width=MAX_LINE_LENGTH))],
        ]
        for code_change in change.code_changes:
            table.append(["", format_diff_table(code_change.before, code_change.after)])
        
        results.append(tabulate(table, tablefmt='rounded_grid', maxcolwidths=[20, None]))
    
    return results