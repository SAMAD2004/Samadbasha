
school_name = "ABC School"   

def show_global():
    print("Inside function (global variable):", school_name)

show_global()
print("Outside function (global variable):", school_name)

def local_example():
    subject = "Math"
    print("Inside function (local variable):", subject)

local_example()

class Student:
    def __init__(self, name, age):
        self.name = name   
        self.age = age    
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

s1 = Student("Alice", 20)
s2 = Student("Bob", 22)

s1.introduce()
s2.introduce()

class Car:
    wheels = 4   

    def __init__(self, brand):
        self.brand = brand  

car1 = Car("Toyota")
car2 = Car("BMW")

print(f"{car1.brand} has {car1.wheels} wheels.")
print(f"{car2.brand} has {car2.wheels} wheels.")
