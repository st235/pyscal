from token import Token, TOKEN_TYPE_EOF, TOKEN_TYPE_INTEGER, TOKEN_TYPE_PLUS, TOKEN_TYPE_MINUS
from typing import Optional

class Interpreter:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_token: Optional[Token] = None
        self.current_char: Optional[str] = self.text[self.pos]

    def error(self):
        raise Exception("Cannot parse input.")

    def advance(self):
        self.pos += 1
        if self.pos >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespaces(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self) -> int:
        token_start_index = self.pos
        while self.current_char is not None and self.current_char.isdigit():
            self.advance()
        return int(self.text[token_start_index:self.pos])

    def get_next_token(self):

        self.skip_whitespaces()

        if self.current_char is None:
            return Token(TOKEN_TYPE_EOF, None)

        if self.current_char.isdigit():
            return Token(TOKEN_TYPE_INTEGER, self.integer())
        elif self.current_char == "+":
            self.advance()
            return Token(TOKEN_TYPE_PLUS, self.current_char)
        elif self.current_char == "-":
            self.advance()
            return Token(TOKEN_TYPE_MINUS, self.current_char)

        self.error()
        return None

    def consume(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
            return

        self.error()

    def match(self, token_type):
        if self.check(token_type):
            self.consume(token_type)
            return True
        return False

    def check(self, token_type) -> bool:
        return self.current_token.type == token_type

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.consume(TOKEN_TYPE_INTEGER)

        op = self.current_token
        if not (self.match(TOKEN_TYPE_PLUS) or
            self.match(TOKEN_TYPE_MINUS)):
            self.error()

        right = self.current_token
        self.consume(TOKEN_TYPE_INTEGER)

        if op.type == TOKEN_TYPE_PLUS:
            result = left.value + right.value
        elif op.type == TOKEN_TYPE_MINUS:
            result = left.value - right.value
        return result
