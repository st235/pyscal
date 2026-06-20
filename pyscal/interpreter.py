from pyscal.scanner import Scanner
from pyscal.lexer import Lexer
from pyscal.tree import BinaryOp, Number, UnaryOp, Compound, Assign, NoOp, Var, Block, Program, Type, VarDecl, VarBlock, \
    ProcedureDecl
from pyscal.visitor import Visitor
from pyscal.symbol_table_builder import SymbolTableBuilder
from pyscal.token import *

class Interpreter(Visitor):
    def __init__(self, text: str):
        self.__lexer = Lexer(Scanner(text))
        self.__sym_table_builder = SymbolTableBuilder()
        self.__globals = {}

    def interpret(self) -> int:
        ast = self.__lexer.parse()
        ast.visit(self.__sym_table_builder)
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
            return left / right
        elif node.op.type == TOKEN_TYPE_INTEGER_DIV:
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
            raise Exception("Unsupported unary op.")

    def visitNumber(self, node: Number):
        return node.token.value

    def visitCompound(self, node: Compound):
        for statement in node.statements:
            statement.visit(self)

    def visitNoOp(self, node: NoOp):
        pass

    def visitAssign(self, node: Assign):
        self.__globals[node.left.value] = node.right.visit(self)

    def visitVar(self, node: Var):
        return self.__globals[node.token.value]

    def visitBlock(self, node: Block):
        for var_decl in node.var_decls:
            var_decl.visit(self)

        node.compound.visit(self)

    def visitProgram(self, node: Program):
        node.block.visit(self)

    def visitType(self, node: Type):
        return node.name

    def visitVarDecl(self, node: VarDecl):
        pass

    def visitVarBlock(self, node: VarBlock):
        pass

    def visitProcedure(self, node: ProcedureDecl):
        pass

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"globals: {self.__globals}"

