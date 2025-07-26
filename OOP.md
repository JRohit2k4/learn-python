## OOP = Object Oriented Programming

**object** = A "bundle" of related attributes (variables) and methods (functions)  
         Ex. phone, car, book, etc.  
         You need a "class" to create many objects

**class** = {blueprint} used to design the structureand layout of an object

```python
class Car:
  def __init__(self, company, model, year, color):
    self.company = company
    self.model = model
    self.year = year
    self.color = color

car1 = Car("Ford", "Mustang", 1969, "Red")
car2 = Car("Chevy", "Camaro", 2022, "Yellow")

#print(f"First car's manufacturer company is: {car1.company}")
#print(f"First car model is: {car1.model}")
#print(f"Manufactured year is: {car1.year}")
#print(f"Color: {car1.color}")

print(f"First car is {car1.year} {car1.color} {car1.company} {car1.model}")
print(f"Second car is {car2.year} {car2.color} {car2.company} {car2.model}")

#Output:
#First car is 1969 Red Ford Mustang
#Second car is 2022 Yellow Chevy Camaro
