## Inheritance
- Allow a class to inherit attributes and methods from another class
- Helps with code reusability and extensibility
- class child(parent)

```python
class Animal: #parent class
  def __init__ (self, name):
    self.name = name

  def eat(self):
    print(f"{self.name} is eating")

  def sleep(self):
    print(f"{self.name} is sleeping")

class Dog(Animal): #child class inheriting parent class attributes
  def speak(self):
    print("WOOF!")

class Cat(Animal):
  def speak(self):
    print("MEOW!")

class Mouse(Animal):
  def speak(self):
    print("SQEEK!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

cat.sleep()
dog.eat()
mouse.speak()
