from abc import ABCMeta, abstractstaticmethod

class Person(metaclass = ABCMeta):

    @abstractstaticmethod
    def person_method():
        """Interface Method"""


class SD (Person):
    def __init__(self):
        self.name = "Nama Sekolah"

    def person_method(self):
        print("Saya Murid SD")


class SMP (Person):
    def __init__(self):
        self.name = "Nama Sekolah"
    
    def person_method(self):
        print("Saya Murid SMP")


class SMA (Person):
    def __init__(self):
        self.name = "Nama Sekolah"

    def person_method(self):
        print("Saya Murid SMA")

class Person_Factory:
    
    @staticmethod
    def build_person(person_type):
        if person_type == "SD":
            return SD()
        
        if person_type == "SMP":
            return SMP()
            
        if person_type == "SMA":
            return SMA()
        
        print("Salah sekolah")
        return -1

if __name__ == "__main__":
    choice = input("Tingkatan siswa yang ingin anda pakai?")
    person = Person_Factory.build_person(choice)
    person.person_method()