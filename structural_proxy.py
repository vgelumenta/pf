from abc import ABCMeta, abstractmethod

class IP(metaclass = ABCMeta):

    @staticmethod
    @abstractmethod
    def person_method():
        """Interface Method"""
    
class Me(IP):
    def person_method(self):
        print("This is me")

class Proxy(IP):

    def __init__(self):
        self.person = Me()
    
    def person_method(self):
        print("This is family")
        self.person.person_method()

p1 = Me()
p1.person_method()

p2 = Proxy()
p2.person_method()