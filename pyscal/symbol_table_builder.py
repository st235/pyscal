from pyscal.symbol import VarSymbol
from pyscal.symbol_table import SymbolTable
from pyscal.tree import *
from pyscal.visitor import Visitor

class SymbolTableBuilder(Visitor):
    def __init__(self):
        self.__symbol_table = SymbolTable()

    def visitBinaryOp(self, node: BinaryOp):
        node.left.visit(self)
        node.right.visit(self)

    def visitUnaryOp(self, node: UnaryOp):
        node.left.visit(self)

    def visitNumber(self, node: Number):
        pass

    def visitCompound(self, node: Compound):
        for statement in node.statements:
            statement.visit(self)

    def visitNoOp(self, node: NoOp):
        pass

    def visitAssign(self, node: Assign):
        var_name = node.left.value
        if self.__symbol_table.lookup(var_name) is None:
            raise Exception(f"Variable {var_name} is not defined")
        node.right.visit(self)

    def visitVar(self, node: Var):
        var_name = node.token.value
        if self.__symbol_table.lookup(var_name) is None:
            raise Exception(f"Variable {var_name} is not defined")

    def visitProgram(self, node: Program):
        node.block.visit(self)

    def visitBlock(self, node: Block):
        for var_declaration in node.var_decls:
            var_declaration.visit(self)
        node.compound.visit(self)

    def visitVarDecl(self, node: VarDecl):
        for var_block in node.blocks:
            var_block.visit(self)

    def visitVarBlock(self, node: VarDecl):
        type_name = node.type.name
        type_symbol = self.__symbol_table.lookup(type_name)
        if type_symbol is None:
            raise Exception(f"Unknown type {type_name}")

        for var_token in node.ids:
            var_name = var_token.value
            if self.__symbol_table.lookup(var_name) is not None:
                raise Exception(f"Redefinition of the existing symbol {var_name}")
            var_symbol = VarSymbol(var_name, type_symbol)
            self.__symbol_table.define(var_symbol)

    def visitType(self, node: Type):
        if self.__symbol_table.lookup(node.name) is None:
            raise Exception(f"Unknown type: {node.name}")

    def visitProcedure(self, node: ProcedureDecl):
        node.block.visit(self)

