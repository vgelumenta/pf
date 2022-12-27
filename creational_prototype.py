from abc import ABCMeta, abstractmethod
import copy

class Course_At_Bimble(metaclass = ABCMeta):

    def __init__(self):
        self.id = None
        self.type = None
    
    @abstractmethod
    def course(self):
        pass

    def get_type(self):
        return self.type
    
    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid
    
    def clone(self):
        return copy.copy(self)
    
#class - SD
class SD(Course_At_Bimble):
    def __init__(self):
        super().__init__()
        self.type = "Sekolah Dasar"

    def course(self):
        print("Inside SD::course() method.")

#class - SMP
class SMP(Course_At_Bimble):
    def __init__(self):
        super().__init__()
        self.type = "Sekolah Menengah Pertama"

    def course(self):
        print("Inside SMP::course() method.")

#class - SMA
class SMA(Course_At_Bimble):
    def __init__(self):
        super().__init__()
        self.type = "Sekolah Menengah Atas"

    def course(self):
        print("Inside SMA::course() method.")

# class - Course At Bimble Chace
class Course_At_Bimble_Chace:

    # chace to store useful information
    chace = {}

    @staticmethod
    def get_course(sid):
        COURSE = Course_At_Bimble_Chace.chace.get(sid, None)
        return COURSE.clone()
    
    @staticmethod
    def load():
        sd = SD()
        sd.set_id("1")
        Course_At_Bimble_Chace.chace[sd.get_id()] = sd

        smp = SMP()
        smp.set_id("2")
        Course_At_Bimble_Chace.chace[smp.get_id()] = smp

        sma = SMA()
        sma.set_id("3")
        Course_At_Bimble_Chace.chace[sma.get_id()] = sma

# main function
if __name__ == "__main__":
    Course_At_Bimble_Chace.load()

    sd = Course_At_Bimble_Chace.get_course("1")
    print(sd.get_type())

    smp = Course_At_Bimble_Chace.get_course("2")
    print(smp.get_type())

    sma = Course_At_Bimble_Chace.get_course("3")
    print(sma.get_type())