from token import Token, TOKEN_TYPE_EOF, TOKEN_TYPE_INTEGER, TOKEN_TYPE_PLUS, TOKEN_TYPE_MINUS
from typing import Optional

class Interpreter:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_token: Optional[Token] = None

    def error(self):
        raise Exception("Cannot parse input.")

    def get_next_token(self):
        text = self.text

        while self.pos < len(text) and text[self.pos].isspace():
            self.pos += 1

        if self.pos >= len(text):
            return Token(TOKEN_TYPE_EOF, None)

        current_char = text[self.pos]

        token_start_index = self.pos
        self.pos += 1

        if current_char.isdigit():
            while self.pos < len(text) and text[self.pos].isdigit():
                self.pos += 1

            return Token(TOKEN_TYPE_INTEGER, int(text[token_start_index:self.pos]))
        elif current_char == "+":
            return Token(TOKEN_TYPE_PLUS, current_char)
        elif current_char == "-":
            return Token(TOKEN_TYPE_MINUS, current_char)

        self.error()

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
