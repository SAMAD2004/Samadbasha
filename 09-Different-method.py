class Student:
    school_name = "ABC School" 

    def __init__(self, name, marks):
        self.name = name       
        self.marks = marks

    def show_details(self):      
        print(f"Name: {self.name}, Marks: {self.marks}")

    @classmethod
    def show_school(cls):
        print(f"School Name: {cls.school_name}")

    @staticmethod
    def welcome():
        print("Welcome to the Student Portal!")


s1 = Student("Rahul", 85)
s2 = Student("Anita", 92)

s1.show_details()
s2.show_details()


Student.show_school()


Student.welcome()
