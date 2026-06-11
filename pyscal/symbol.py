from __future__ import annotations
from typing import Optional

class Symbol:
    def __init__(self, name: str, type: Optional[Symbol] = None):
        self.name = name.lower()
        self.type = type

class BuiltinTypeSymbol(Symbol):
    def __init__(self, name: str):
        super().__init__(name)

    def __str__(self):
        return f"<builtin type {self.name}>"

    def __repr__(self):
        return str(self)

class VarSymbol(Symbol):
    def __init__(self, name: str, type: BuiltinTypeSymbol):
        super().__init__(name, type)

    def __str__(self):
        return f"<{self.name}:{self.type}>"

    def __repr__(self):
        return str(self)
