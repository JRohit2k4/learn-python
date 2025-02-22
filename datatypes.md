# 📌 Data Types in Python

## **Types of Data Types in Python**
Python has several built-in data types including **numeric, sequence, mapping, boolean, set, and binary types**.

- **Numeric types**: `int`, `float`, `complex`
- **Sequence types**: `str`, `list`, `tuple`, `range`
- **Mapping types**: `dict`
- **Boolean types**: `bool`
- **Set types**: `set`, `frozenset`

## 🔹 **1. Numeric Types**
Numeric types include `int`, `float`, and `complex`.

### ▫ **Integer (`int`)**
Represents whole numbers (positive or negative) without decimals.
```python
num = 10
print(type(num))  # Output: <class 'int'>
```

### ▫ **Float (`float`)**
Represents decimal numbers.
```python
pi = 3.14
print(type(pi))  # Output: <class 'float'>
```

### ▫ **Complex (`complex`)**
Represents complex numbers with a real and imaginary part.
```python
c = 2 + 3j
print(type(c))  # Output: <class 'complex'>
```

## 🔹 **2. Sequence Types**
Sequence types include `str`, `list`, `tuple`, and `range`.

### ▫ **String (`str`)**
Represents a sequence of characters enclosed in quotes.
```python
name = "Python"
print(type(name))  # Output: <class 'str'>
```

### ▫ **List (`list`)**
Ordered, **mutable** collection of elements.
```python
fruits = ["apple", "banana", "cherry"]
print(type(fruits))  # Output: <class 'list'>
```

### ▫ **Tuple (`tuple`)**
Ordered, **immutable** collection of elements.
```python
coordinates = (10, 20)
print(type(coordinates))  # Output: <class 'tuple'>
```

### ▫ **Range (`range`)**
Represents an immutable sequence of numbers.
```python
r = range(5)
print(type(r))  # Output: <class 'range'>
```

## 🔹 **3. Mapping Type**
Mapping types include `dict`.

### ▫ **Dictionary (`dict`)**
Unordered collection of **key-value pairs**.
```python
person = {"name": "Rohit", "age": 21}
print(type(person))  # Output: <class 'dict'>
```

## 🔹 **4. Boolean Type**
Boolean types include `bool`.

### ▫ **Boolean (`bool`)**
Represents either `True` or `False` values.
```python
is_python_fun = True
print(type(is_python_fun))  # Output: <class 'bool'>
```

## 🔹 **5. Set Types**
Set types include `set` and `frozenset`.

### ▫ **Set (`set`)**
Unordered collection of **unique** elements.
```python
unique_numbers = {1, 2, 3, 3, 4}
print(type(unique_numbers))  # Output: <class 'set'>
```

### ▫ **Frozen Set (`frozenset`)**
Immutable version of a set.
```python
fset = frozenset([1, 2, 3, 3, 4])
print(type(fset))  # Output: <class 'frozenset'>
```

## 🔹 **6. None Type**
Represents **no value** or **null**.
```python
nothing = None
print(type(nothing))  # Output: <class 'NoneType'>
```

## ✅ **Summary**
| Data Type  | Description  | Example  |
|------------|-------------|----------|
| `int`      | Whole numbers | `10, -5, 1000` |
| `float`    | Decimal numbers | `3.14, -0.5, 2.0` |
| `str`      | Text/characters | `'Python'`, `'Hello'` |
| `bool`     | True/False values | `True, False` |
| `list`     | Mutable collection | `[1, 2, 3]` |
| `tuple`    | Immutable collection | `(1, 2, 3)` |
| `dict`     | Key-value pairs | `{'name': 'Rohit', 'age': 21}` |
| `set`      | Unique unordered elements | `{1, 2, 3}` |
| `NoneType` | Represents no value | `None` |

---
🔹 **Next, we will cover Operators in Python!** 🚀
