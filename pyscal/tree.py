from abc import ABC, abstractmethod
from typing import List

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


class UnaryOp(AST):
    def __init__(self, left: AST, op: Token):
        self.left = left
        self.op = op

    def visit(self, visitor: "Visitor"):
        return visitor.visitUnaryOp(self)


class Number(AST):
    def __init__(self, token: Token):
        self.token = token

    def visit(self, visitor: "Visitor"):
        return visitor.visitNumber(self)

class Compound(AST):
    def __init__(self, statements: List[AST]):
        self.statements = statements

    def visit(self, visitor: "Visitor"):
        return visitor.visitCompound(self)

class NoOp(AST):
    def __init__(self):
        pass

    def visit(self, visitor: "Visitor"):
        return visitor.visitNoOp(self)

class Assign(AST):
    def __init__(self, left: Token, right: AST):
        self.left = left
        self.right = right

    def visit(self, visitor: "Visitor"):
        return visitor.visitAssign(self)

class Var(AST):
    def __init__(self, token: Token):
        self.token = token

    def visit(self, visitor: "Visitor"):
        return visitor.visitVar(self)
