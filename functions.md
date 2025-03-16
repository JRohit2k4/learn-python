### **Functions in Python**  

A function in Python is a **block of reusable code** that performs a specific task. It helps in organizing code, improving readability, and reducing redundancy.  

---

### **Types of Functions in Python**  

1. **Built-in Functions**:  
   - These are pre-defined in Python (e.g., `print()`, `len()`, `type()`).  
   - Example:  
     ```python
     print(len("Hello"))  # Output: 5
     ```
  
2. **User-defined Functions**:  
   - Functions created by users to perform specific tasks.  
   - Example:  
     ```python
     def greet(name):
         return f"Hello, {name}!"
     
     print(greet("Rohit"))  # Output: Hello, Rohit!
     ```

3. **Lambda Functions (Anonymous Functions)**:  
   - Small, one-line functions using the `lambda` keyword.  
   - Example:  
     ```python
     add = lambda x, y: x + y
     print(add(5, 3))  # Output: 8
     ```

---

### **Function Structure in Python**  

A function typically follows this structure:  

```python
def function_name(parameters):  
    """Optional docstring explaining the function"""
    # Function body (logic)
    return value  # Optional return statement
```

Example:  
```python
def add_numbers(a, b):  
    """Returns the sum of two numbers"""  
    return a + b  

result = add_numbers(10, 20)  
print(result)  # Output: 30  
```

---

### **Arguments and Parameters**  

- **Positional Arguments** (Order matters)  
  ```python
  def greet(name, age):
      print(f"Hello {name}, you are {age} years old.")

  greet("Rohit", 21)  # Correct
  # greet(21, "Rohit")  # Incorrect order
  ```

- **Default Parameters** (If not provided, uses default)  
  ```python
  def greet(name="Guest"):
      print(f"Hello {name}!")

  greet()  # Output: Hello Guest!
  greet("Rohit")  # Output: Hello Rohit!
  ```

- **Keyword Arguments** (Pass by name)  
  ```python
  def greet(name, age):
      print(f"Hello {name}, you are {age} years old.")

  greet(age=21, name="Rohit")  # Order doesn't matter
  ```

- **Arbitrary Arguments (`*args`)** (Multiple positional arguments)  
  ```python
  def add_all(*numbers):
      return sum(numbers)

  print(add_all(1, 2, 3, 4))  # Output: 10
  ```

- **Arbitrary Keyword Arguments (`**kwargs`)** (Multiple named arguments)  
  ```python
  def person_info(**info):
      for key, value in info.items():
          print(f"{key}: {value}")

  person_info(name="Rohit", age=21, city="Delhi")
  ```

---

### **Returning Values from Functions**  
- A function can return a value using the `return` statement.  
- If there is no `return`, the function returns `None`.  

```python
def square(num):
    return num * num

result = square(4)
print(result)  # Output: 16
```

---

### **Why Use Functions?**
✅ **Code Reusability**  
✅ **Modularity (Divides code into smaller tasks)**  
✅ **Readability & Maintainability**  
✅ **Avoids Code Duplication**  
