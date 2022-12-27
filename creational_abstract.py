import random

class Course_At_Bimble:

    """ Bimble portal for course """

    def __init__(self, course_factory = None):
        """course factory is out abstract factory"""

        self.course_factory = course_factory
    
    def show_course(self):

        """creates and shows course using the abstract factory"""

        course = self.course_factory()

        print(f'Kami memiliki kursus tingkat {course}')
        print(f'dengan harga {course.price()}')

class SD:

    """ Kelas untuk Sekolah Dasar """

    def price(self):
        return 40000

    def __str__(self):
        return "SD"

class SMP:

    """ Kelas untuk Sekolah Menengah Pertama """

    def price(self):
        return 45000

    def __str__(self):
        return "SMP"

class SMA:

    """ Kelas untuk Sekolah Menengah Atas """

    def price(self):
        return 50000

    def __str__(self):
        return "SMA"

# main method
if __name__ == "__main__":
    sd = SD() # objek untuk kelas SD
    smp = SMP() # objek untuk kelas SMP
    sma = SMA() # objek untuk kelas SMA

    print(f'Nama Kelasnya adalah {sd} dan harganya {sd.price()}')
    print(f'Nama Kelasnya adalah {smp} dan harganya {smp.price()}')
    print(f'Nama Kelasnya adalah {sma} dan harganya {sma.price()}')

def random_course():

    """A random class for choosing the course"""

    return random.choice([SD, SMP, SMA])()


if __name__ == "__main__":

    course = Course_At_Bimble(random_course)

    for i in range(5):
        course.show_course()