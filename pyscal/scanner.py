from pyscal.token import *

from typing import Optional

class Scanner:
    def __init__(self, text: str):
        self.__text = text
        self.__pos = 0
        self.__current_char: Optional[str] = self.__text[self.__pos]

    def error(self):
        raise Exception("Cannot parse input.")

    def advance(self):
        self.__pos += 1
        if self.__pos >= len(self.__text):
            self.__current_char = None
        else:
            self.__current_char = self.__text[self.__pos]

    def skip_whitespaces(self):
        while self.__current_char is not None and self.__current_char.isspace():
            self.advance()

    def integer(self) -> int:
        token_start_index = self.__pos
        while self.__current_char is not None and self.__current_char.isdigit():
            self.advance()
        return int(self.__text[token_start_index:self.__pos])

    def get_next_token(self):
        self.skip_whitespaces()

        if self.__current_char is None:
            return Token(TOKEN_TYPE_EOF, None)

        if self.__current_char.isdigit():
            return Token(TOKEN_TYPE_INTEGER, self.integer())
        elif self.__current_char == "+":
            self.advance()
            return Token(TOKEN_TYPE_PLUS, self.__current_char)
        elif self.__current_char == "-":
            self.advance()
            return Token(TOKEN_TYPE_MINUS, self.__current_char)
        elif self.__current_char == "*":
            self.advance()
            return Token(TOKEN_TYPE_STAR, self.__current_char)
        elif self.__current_char == "/":
            self.advance()
            return Token(TOKEN_TYPE_SLASH, self.__current_char)

        self.error()
        return None
