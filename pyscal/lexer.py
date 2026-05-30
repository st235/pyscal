from pyscal.scanner import Scanner
from pyscal.token import *
from pyscal.tree import AST, BinaryOp, Number

from typing import Optional

class Lexer:
    def __init__(self, scanner: Scanner):
        self.__scanner: Scanner = scanner
        self.__current_token: Optional[Token] = self.__scanner.get_next_token()

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

    def parse(self):
        result = self.expr()
        self.consume(TOKEN_TYPE_EOF)
        return result

    def expr(self) -> AST:
        return self.term()

    def term(self) -> AST:
        left = self.factor()

        while self.__current_token.type in (TOKEN_TYPE_PLUS, TOKEN_TYPE_MINUS):
            op = self.__current_token
            self.match(TOKEN_TYPE_PLUS) or self.match(TOKEN_TYPE_MINUS)

            left = BinaryOp(left, op, self.factor())

        return left

    def factor(self) -> AST:
        left = self.primary()

        while self.__current_token.type in (TOKEN_TYPE_STAR, TOKEN_TYPE_SLASH):
            op = self.__current_token
            self.match(TOKEN_TYPE_STAR) or self.match(TOKEN_TYPE_SLASH)
            left = BinaryOp(left, op, self.primary())

        return left

    def primary(self) -> AST:
        if self.check(TOKEN_TYPE_INTEGER):
            result = Number(self.__current_token)
            self.consume(TOKEN_TYPE_INTEGER)
        else:
            self.consume(TOKEN_TYPE_LEFT_PAREN)
            result = self.expr()
            self.consume(TOKEN_TYPE_RIGHT_PAREN)
        return result
