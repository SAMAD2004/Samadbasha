class Student:
    
    school_name = "ABC School"

    def __init__(self, name, age):
     
        self.name = name
        self.age = age

s1 = Student("Alice", 14)
s2 = Student("Bob", 15)
print("Student 1:", s1.name, "-", s1.age)
print("Student 2:", s2.name, "-", s2.age)

# Access static variable (same for all)
print("School Name (via class):", Student.school_name)
print("School Name (via object):", s1.school_name)

# Changing instance variable (only for that object)
s1.age = 16
print("Updated Student 1 age:", s1.age)
print("Student 2 age (unchanged):", s2.age)

# Changing static variable (affects all objects)
Student.school_name = "XYZ School"
print("Updated School Name (via Student):", Student.school_name)
print("School Name (via s2):", s2.school_name)
