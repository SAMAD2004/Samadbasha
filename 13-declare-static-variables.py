class Car:
  
    wheels = 4   
    brand = "Generic"

    def __init__(self, model, color):
     
        self.model = model
        self.color = color


print("Number of wheels:", Car.wheels)
print("Brand:", Car.brand)

c1 = Car("Sedan", "Red")
c2 = Car("SUV", "Blue")

print("Car 1 brand:", c1.brand)
print("Car 2 brand:", c2.brand)

Car.brand = "Toyota"
print("Updated Brand:", Car.brand)
print("Car 1 brand after update:", c1.brand)
print("Car 2 brand after update:", c2.brand)
