from dataclasses import dataclass
from typing import List, Optional

@dataclass
class TextRange:
    first_line: int
    first_col: int
    last_line: int
    last_col: int

@dataclass
class SingleChange:

    @dataclass
    class Location:
        removed: Optional[TextRange]
        added: Optional[TextRange]

    short_desc: str
    long_desc: str
    locations: List[Location]



