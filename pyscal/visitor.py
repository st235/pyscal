from abc import ABC, abstractmethod

from pyscal.tree import BinaryOp, Number


class Visitor(ABC):

    @abstractmethod
    def visitBinaryOp(self, node: BinaryOp):
        ...

    @abstractmethod
    def visitNumber(self, node: Number):
        ...