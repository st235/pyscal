from abc import ABC, abstractmethod

from pyscal.tree import *


class Visitor(ABC):

    @abstractmethod
    def visitBinaryOp(self, node: BinaryOp):
        ...

    @abstractmethod
    def visitUnaryOp(self, node: UnaryOp):
        ...

    @abstractmethod
    def visitNumber(self, node: Number):
        ...

    @abstractmethod
    def visitCompound(self, node: Compound):
        ...

    @abstractmethod
    def visitNoOp(self, node: NoOp):
        ...

    @abstractmethod
    def visitAssign(self, node: Assign):
        ...

    @abstractmethod
    def visitVar(self, node: Var):
        ...

    @abstractmethod
    def visitProgram(self, node: Program):
        ...

    @abstractmethod
    def visitBlock(self, node: Block):
        ...


    @abstractmethod
    def visitVarDecl(self, node: VarDecl):
        ...

    @abstractmethod
    def visitType(self, node: Type):
        ...

