from pyscal.token import *

from typing import Optional

_PREDEFINED_KEYWORDS_LOOKUP = {
    "begin": TOKEN_TYPE_BEGIN,
    "end": TOKEN_TYPE_END,
    "program": TOKEN_TYPE_PROGRAM,
    "var": TOKEN_TYPE_VAR,
    "integer": TOKEN_TYPE_INTEGER,
    "real": TOKEN_TYPE_REAL,
    "div": TOKEN_TYPE_INTEGER_DIV,
    "procedure": TOKEN_TYPE_PROCEDURE,
}

class Scanner:
    def __init__(self, text: str):
        self.__text = text
        self.__pos = 0
        self.__current_char: Optional[str] = self.__text[self.__pos]

    def error(self):
        raise Exception("Cannot parse input.")

    def peek(self) -> Optional[str]:
        if self.__pos + 1 >= len(self.__text):
            return None
        return self.__text[self.__pos + 1]

    def advance(self):
        self.__pos += 1
        if self.__pos >= len(self.__text):
            self.__current_char = None
        else:
            self.__current_char = self.__text[self.__pos]

    def skip_whitespaces(self):
        while self.__current_char is not None and self.__current_char.isspace():
            self.advance()

    def skip_comments(self):
        if self.__current_char != "{":
            return

        # {
        self.advance()
        while self.__current_char is not None and self.__current_char != "}":
            self.advance()
        # }
        self.advance()


    def __isalphaspecial(self) -> bool:
        return self.__current_char is not None and (self.__current_char == "_" or self.__current_char.isalpha())

    def __id(self) -> Token:
        token_start_index = self.__pos
        while (self.__current_char is not None and
               (self.__isalphaspecial() or self.__current_char.isdigit())):
            self.advance()

        identifier = self.__text[token_start_index:self.__pos].lower()
        if identifier in _PREDEFINED_KEYWORDS_LOOKUP:
            return Token(_PREDEFINED_KEYWORDS_LOOKUP[identifier], identifier)

        return Token(TOKEN_TYPE_ID, identifier)

    def __number(self) -> Token:
        token_start_index = self.__pos
        is_real = False

        while (self.__current_char is not None and
               self.__current_char.isdigit() or
                self.__current_char == "."):
            if self.__current_char == ".":
                if is_real:
                    raise Exception("Cannot recognize number.")
                is_real = True
            self.advance()

        if is_real:
            return Token(TOKEN_TYPE_REAL_CONST, float(self.__text[token_start_index:self.__pos]))
        else:
            return Token(TOKEN_TYPE_INTEGER_CONST, int(self.__text[token_start_index:self.__pos]))

    def get_next_token(self):
        while self.__current_char is not None and \
                (self.__current_char.isspace() or self.__current_char == "{"):
            if self.__current_char.isspace():
                self.skip_whitespaces()
            else:
                self.skip_comments()

        if self.__current_char is None:
            return Token(TOKEN_TYPE_EOF, None)

        if self.__current_char.isdigit():
            return self.__number()

        if self.__isalphaspecial():
            return self.__id()

        if self.__current_char == "+":
            self.advance()
            return Token(TOKEN_TYPE_PLUS, "+")
        elif self.__current_char == "-":
            self.advance()
            return Token(TOKEN_TYPE_MINUS, "-")
        elif self.__current_char == "*":
            self.advance()
            return Token(TOKEN_TYPE_STAR, "*")
        elif self.__current_char == "/":
            self.advance()
            return Token(TOKEN_TYPE_SLASH, "/")
        elif self.__current_char == "(":
            self.advance()
            return Token(TOKEN_TYPE_LEFT_PAREN, "(")
        elif self.__current_char == ")":
            self.advance()
            return Token(TOKEN_TYPE_RIGHT_PAREN, ")")
        elif self.__current_char == ".":
            self.advance()
            return Token(TOKEN_TYPE_DOT, ".")
        elif self.__current_char == ";":
            self.advance()
            return Token(TOKEN_TYPE_SEMI, ":")
        elif self.__current_char == ",":
            self.advance()
            return Token(TOKEN_TYPE_COMMA, ",")
        elif self.__current_char == ":":
            self.advance()

            if self.__current_char == "=":
                self.advance()
                return Token(TOKEN_TYPE_ASSIGN, ":=")
            else:
                return Token(TOKEN_TYPE_COLON, ":")

        self.error()
        return None
