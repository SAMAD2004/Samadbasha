class Student:
 
    def __init__(self, name, age):
        self.name = name     
        self.age = age      


    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Alice", 20)
s2 = Student("Bob", 22)


s1.display()
s2.display()
