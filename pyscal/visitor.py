from abc import ABC, abstractmethod

from pyscal.tree import BinaryOp, UnaryOp, Number


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
