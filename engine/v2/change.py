from dataclasses import dataclass
from typing import List, Optional

@dataclass 
class SingleChange:

    @dataclass 
    class CodeChange:
        before: Optional[str]
        after: Optional[str]

    short_desc: str
    long_desc: str
    code_changes: List[CodeChange]
    