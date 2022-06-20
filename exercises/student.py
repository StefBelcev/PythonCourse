class Student:
    """Kreiranje na klasa student"""

    def __init__(self, n, a, f, b):
        self.full_name = n
        self.age = a
        self.faculty = f
        self.birthday = b

    def get_age(self):
        return self.age

    def get_name(self):
        return self.full_name

    def get_birth(self):
        return self.birthday

    def get_faculty(self):
        return self.faculty


class AIStudent(Student):
    """"""

    def __init__(self, n, a, f, b, s):
        super(AIStudent, self).__init__(n, a, f, b)
        self.s = s


class Sample:
    """Primer od predavanje za klasni atriburi"""
    x = 23

    def increment(self):
        self.__class__.x += 1


class Counter:
    """"""

    # klasen atribut
    overall_total = 0

    def __init__(self):
        self.my_total = 0  # podatocen atribut

    def increment(self):
        Counter.overall_total = Counter.overall_total + 1
        self.my_total = self.my_total + 1


if __name__ == '__main__':
    b = Student('Marko', 21, "FINKI", "02/02/1998")
    f = Student("Bob Smith", 23, "Ekonomski", "03/03/1997")
    # Dobivanje na ime, vozrast vo vreme na izvrshuvanje
    getattr(f, "full_name")
    getattr(f, "age")
    getattr(f, "get_age")()  # vaka se povikuva funckija
    # hasattr
    hasattr(f, "full_name")
    print(b.full_name)  # pristapi promenliva
    print(b.get_age())  # pristapi do metod
    print("Ime i vozrast na studentot: " + b.get_name(), b.get_age())

    a = Sample()
    b = Sample()
    print(a.__class__.x)
    a.increment()
    print(a.__class__.x)
    b.increment()
    print(b.__class__.x)
    c = Sample()
    c.increment()
    print(c.__class__.x)
