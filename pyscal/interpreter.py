from pyscal.scanner import Scanner
from pyscal.lexer import Lexer

class Interpreter:
    def __init__(self, text: str):
        self.__lexer = Lexer(Scanner(text))

    def expr(self) -> int:
        return self.__lexer.parse()
