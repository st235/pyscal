from typing import Dict, Optional

from pyscal.symbol import Symbol, BuiltinTypeSymbol

class SymbolTable:
    def __init__(self):
        self.__symbols: Dict[str, Symbol] = {}
        self.__init_builtins()

    def __init_builtins(self):
        self.define(BuiltinTypeSymbol("INTEGER"))
        self.define(BuiltinTypeSymbol("REAL"))

    def define(self, symbol: Symbol):
        self.__symbols[symbol.name] = symbol

    def lookup(self, name: str) -> Optional[Symbol]:
        return self.__symbols.get(name.lower(), None)

    def __str__(self):
        return f"Defined symbols: {[v for v in self.__symbols.values()]}"

    def __repr__(self):
        return str(self)
