TOKEN_TYPE_INTEGER = "INTEGER"
TOKEN_TYPE_PLUS = "PLUS"
TOKEN_TYPE_MINUS = "MINUS"
TOKEN_TYPE_STAR = "STAR"
TOKEN_TYPE_SLASH = "SLASH"
TOKEN_TYPE_LEFT_PAREN = "LEFT_PAREN"
TOKEN_TYPE_RIGHT_PAREN = "RIGHT_PAREN"
TOKEN_TYPE_EOF = "EOF"

class Token:
    def __init__(self, type: str, value: int):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {self.value})"

    def __repr__(self):
        return str(self)
