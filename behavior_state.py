from abc import ABCMeta, abstractmethod

class Context():

    def __init__(self):

        self.state_handles = [
            Started(),
            Running(),
            Finished()
        ]
        self._handle = iter(self.state_handles)

    def request(self):
        try:
            self._handle.__next__()()
        except StopIteration:
            self._handle = iter(self.state_handles)


class IState(metaclass=ABCMeta):
    "A State Interface"
    @staticmethod
    @abstractmethod
    def __call__():
        "Set the default method"

class Started(IState):

    @staticmethod
    def method():
        print("Task Started")

    __call__ = method


class Running(IState):

    @staticmethod
    def method():
        print("Task Running")

    __call__ = method


class Finished(IState):

    @staticmethod
    def method():
        print("Task Finished")

    __call__ = method


CONTEXT = Context()
CONTEXT.request()
CONTEXT.request()
CONTEXT.request()
CONTEXT.request()
CONTEXT.request()
CONTEXT.request()