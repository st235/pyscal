from pyscal.scanner import Scanner
from pyscal.token import *
from typing import Optional

class Lexer:
    def __init__(self, scanner: Scanner):
        self.__scanner: Scanner = scanner
        self.__current_token: Optional[Token] = None

    def error(self):
        raise Exception("Cannot parse input.")

    def consume(self, token_type):
        if self.__current_token.type == token_type:
            self.__current_token = self.__scanner.get_next_token()
            return

        self.error()

    def match(self, token_type):
        if self.check(token_type):
            self.consume(token_type)
            return True
        return False

    def check(self, token_type) -> bool:
        return self.__current_token.type == token_type

    def expr(self) -> int:
        self.__current_token = self.__scanner.get_next_token()
        return self.term()

    def term(self) -> int:
        left = self.factor()

        while self.__current_token.type in (TOKEN_TYPE_PLUS, TOKEN_TYPE_MINUS):
            op = self.__current_token
            self.match(TOKEN_TYPE_PLUS) or self.match(TOKEN_TYPE_MINUS)

            right = self.factor()

            if op.type == TOKEN_TYPE_PLUS:
                left = left + right
            elif op.type == TOKEN_TYPE_MINUS:
                left = left - right

        return left

    def factor(self) -> int:
        left = self.__current_token.value
        self.consume(TOKEN_TYPE_INTEGER)

        while self.__current_token.type in (TOKEN_TYPE_STAR, TOKEN_TYPE_SLASH):
            op = self.__current_token
            self.match(TOKEN_TYPE_STAR) or self.match(TOKEN_TYPE_SLASH)

            right = self.__current_token.value
            self.consume(TOKEN_TYPE_INTEGER)

            if op.type == TOKEN_TYPE_STAR:
                left = left * right
            elif op.type == TOKEN_TYPE_SLASH:
                left = left / right

        return left
