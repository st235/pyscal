from abc import ABC, abstractmethod

from pyscal.tree import BinaryOp, UnaryOp, Number, Compound, NoOp, Assign, Var


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
