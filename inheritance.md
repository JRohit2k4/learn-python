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
```

## Multiple inheritance  
- Inherit from more than one parent class.  
- ex. C(A, B)
```python
class Prey:
  def flee(self):
    print("animal is fleeing")

class Predator:
  def hunt(self):
    print("animal is hunting")

class Rabbit(Prey): #only inherit prey class
  pass

class Hawk(Predator): #only inherits predator class
  pass

class Fish(Prey, Predator): #inherits both prey and prey class
  pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
```

## Multilevel inheritance  
- Inherit from a parent which inherits from parent.  
- ex. C(B) <- B(A) <- A
