class Student:
    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def introduce(self):  
        return f"My name is {self.name} and I am {self.age} years old."

s1 = Student("Rahul", 21)
print(s1.introduce())  