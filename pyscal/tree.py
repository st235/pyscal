from abc import ABC, abstractmethod

from pyscal.token import Token

class AST(ABC):

    @abstractmethod
    def visit(self, visitor: "Visitor"):
        ...


class BinaryOp(AST):
    def __init__(self, left: AST, op: Token, right: AST):
        self.left = left
        self.op = op
        self.right = right

    def visit(self, visitor: "Visitor"):
        return visitor.visitBinaryOp(self)

class Number(AST):
    def __init__(self, token: Token):
        self.token = token

    def visit(self, visitor: "Visitor"):
        return visitor.visitNumber(self)
