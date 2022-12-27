from abc import ABCMeta, abstractmethod

class IA(metaclass = ABCMeta):
    @staticmethod
    @abstractmethod
    def method_a():
        """An Abstract method A"""

class English(IA):
    def method_a(self):
        print("This is English")


class IB(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method_b():
        """An Abstract method B"""

class Indonesian(IB):
    def method_b(swlf):
        print("This is Indonesia")

class ClassBAdapter(IA):
    def __init__(self):
        self.classB = Indonesian()

    def method_a(self):
        """Calls class Indonesia"""
        self.classB.method_b()
    
Item = ClassBAdapter()
Item.method_a()