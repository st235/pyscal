from pyscal.scanner import Scanner
from pyscal.lexer import Lexer
from pyscal.tree import BinaryOp, Number, UnaryOp
from pyscal.visitor import Visitor
from pyscal.token import *

class Interpreter(Visitor):
    def __init__(self, text: str):
        self.__lexer = Lexer(Scanner(text))

    def expr(self) -> int:
        ast = self.__lexer.parse()
        return ast.visit(self)

    def visitBinaryOp(self, node: BinaryOp):
        left = node.left.visit(self)
        right = node.right.visit(self)

        if node.op.type == TOKEN_TYPE_PLUS:
            return left + right
        elif node.op.type == TOKEN_TYPE_MINUS:
            return left - right
        elif node.op.type == TOKEN_TYPE_STAR:
            return left * right
        elif node.op.type == TOKEN_TYPE_SLASH:
            return left // right
        else:
            raise Exception("Unsupported binary op.")

    def visitUnaryOp(self, node: UnaryOp):
        left = node.left.visit(self)

        if node.op.type == TOKEN_TYPE_PLUS:
            return left
        elif node.op.type == TOKEN_TYPE_MINUS:
            return -left
        else:
            raise Exception("Unsuported unary op.")

    def visitNumber(self, node: Number):
        return node.token.value

