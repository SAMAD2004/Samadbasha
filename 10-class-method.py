class Student:
    school_name = "ABC School" 

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_school(cls):
        print(f"School Name: {cls.school_name}")


Student.show_school()

s1 = Student("Rahul")
s1.show_school()
