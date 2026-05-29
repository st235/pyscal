from scanner import Scanner
from lexer import Lexer

class Interpreter:
    def __init__(self, text: str):
        self.__lexer = Lexer(Scanner(text))

    def expr(self) -> int:
        return self.__lexer.expr()
