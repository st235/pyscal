from pyscal.scanner import Scanner
from pyscal.token import *
from pyscal.tree import AST, BinaryOp, Number, UnaryOp, Compound, NoOp, Assign, Var

from typing import Optional, List

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
        result = self.program()
        self.consume(TOKEN_TYPE_EOF)
        return result

    def program(self) -> AST:
        node = self.compound_statement()
        self.consume(TOKEN_TYPE_DOT)
        return node

    def compound_statement(self) -> AST:
        self.consume(TOKEN_TYPE_BEGIN)
        compound = Compound(self.statement_list())
        self.consume(TOKEN_TYPE_END)
        return compound

    def statement_list(self) -> List[AST]:
        statements = [self.statement()]

        while self.match(TOKEN_TYPE_SEMI):
            statements.append(self.statement())

        return statements

    def statement(self) -> AST:
        if self.check(TOKEN_TYPE_BEGIN):
            return self.compound_statement()
        elif self.check(TOKEN_TYPE_ID):
            return self.assignment_statement()
        else:
            return self.empty()

    def assignment_statement(self) -> AST:
        variable = self.__current_token
        self.consume(TOKEN_TYPE_ID)
        self.consume(TOKEN_TYPE_ASSIGN)

        return Assign(variable, self.expr())

    def empty(self) -> AST:
        return NoOp()

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
        prev = self.__current_token
        if self.check(TOKEN_TYPE_INTEGER):
            result = Number(self.__current_token)
            self.consume(TOKEN_TYPE_INTEGER)
        elif self.match(TOKEN_TYPE_LEFT_PAREN):
            result = self.expr()
            self.consume(TOKEN_TYPE_RIGHT_PAREN)
        elif self.match(TOKEN_TYPE_PLUS):
            result = UnaryOp(self.primary(), prev)
        elif self.match(TOKEN_TYPE_MINUS):
            result = UnaryOp(self.primary(), prev)
        else:
            self.consume(TOKEN_TYPE_ID)
            return Var(prev)

        return result
