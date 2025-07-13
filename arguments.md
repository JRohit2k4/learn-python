## What are Arguments?
When you define function you can pass values (arguments) into it so it can use them internally.

```python
def greet(name):
  print(f"Hello, {name}")

greet("Rohit")
# Hello, Rohit
```

## Types of Arguments


## 1.Positional Argument  
Values are passed in the **same order** as parameters.  
```python
def net_price(list_price, discount, tax)
    return list_price * (1-discount) * (1+tax)

net_price(500,0.5,0.1)
```

## 2.Default Arguments
A default parameters default is used when that argument is omitted make your functions more flexible, reduces number of arguments.
```python
def net_price(list_price, discount=0.5, tax=0.1)
    return list_price * (1-discount) * (1+tax)

net_price(500)
```

## 3.Keyword Arguments
You can pass argumnets **by name**, not just by position.
```python
def student_info(name, age):
    print(f"{name} is {age} years old.")

student_info(age=20, name="Rohit")
```

## 4.Variable-length Positional Arguments(*args)
Use *args when you **don't know** how many arguments you'll receive.

```python
def total_marks(*args)
  print("Total: ",sum(args))

total_marks(80,90,70)
 # Total: 240
```
