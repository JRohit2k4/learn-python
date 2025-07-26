## OOP = Object Oriented Programming

**object** = A "bundle" of related attributes (variables) and methods (functions)  
         Ex. phone, car, book, etc.  
         You need a "class" to create many objects

**class** = {blueprint} used to design the structureand layout of an object

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Supra")
print(my_car.brand)
# Output: Toyota
