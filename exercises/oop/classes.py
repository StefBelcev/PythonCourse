if __name__ == "__main__":
    klasa = 'Kreiranje klasi'
    print(klasa)
    class Student:
        """Klasa za reprezentacija na student"""
        def __init__(self, n, a):
            self.full_name = n
            self.age = a
        def get_age(self):
            return self.age
        def get_full_name(self):
            return self.full_name
    class AIStudent(Student):
        def __init__(self,n,a,s):
            super(AIStudent, self).__init__(n,a) #call init for Student
            self.section_num = s
        def get_age(self):
            return self.age

    student = Student('Stefan Belchev', 23)
    #using get methods
    student_age = student.get_age()
    student_full_name = student.get_full_name()
    print(f'Name of the student:',student_full_name)
    print(f'Age of the student:', student_age)
    #using variables name
    print('Name:', student.full_name)
    print('Age:', student.age)
    #using getattr
    print('Name using get attribute ()',getattr(student,'full_name'))
    age=getattr(student,"get_age")()
    print(f'Age using get attribute', age)
    print(hasattr(student,'birthday')) if hasattr(student,'birthday') else print('sex on the beach!')