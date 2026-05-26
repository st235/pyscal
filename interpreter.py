from token import Token, EOF, INTEGER, PLUS
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
            return Token(EOF, None)

        current_char = text[self.pos]

        token_start_index = self.pos
        self.pos += 1

        if current_char.isdigit():
            while self.pos < len(text) and text[self.pos].isdigit():
                self.pos += 1

            return Token(INTEGER, int(text[token_start_index:self.pos]))
        elif current_char == "+":
            return Token(PLUS, current_char)

        self.error()

    def consume(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
            return

        self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.consume(INTEGER)

        op = self.current_token
        self.consume(PLUS)

        right = self.current_token
        self.consume(INTEGER)

        result = left.value + right.value
        return result
