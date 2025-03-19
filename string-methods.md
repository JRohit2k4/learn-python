# Python String Methods

Python provides several built-in methods to manipulate strings. Below is a list of commonly used string methods with examples.

---


### `upper()` - Converts all characters to uppercase
```python
text = "hello world"
print(text.upper())  # Output: HELLO WORLD
```

### `lower()` - Converts all characters to lowercase
```python
text = "Hello World"
print(text.lower())  # Output: hello world
```

### `title()` - Converts the first letter of each word to uppercase
```python
text = "hello world"
print(text.title())  # Output: Hello World
```

### `capitalize()` - Capitalizes the first letter of the string
```python
text = "hello world"
print(text.capitalize())  # Output: Hello world
```

### `swapcase()` - Swaps uppercase to lowercase and vice versa
```python
text = "Hello World"
print(text.swapcase())  # Output: hELLO wORLD
```

---


### `startswith(substring)` - Checks if the string starts with the given substring
```python
text = "Python is fun"
print(text.startswith("Python"))  # Output: True
```

### `endswith(substring)` - Checks if the string ends with the given substring
```python
text = "Python is fun"
print(text.endswith("fun"))  # Output: True
```

### `isalpha()` - Returns `True` if all characters are letters
```python
text = "Hello"
print(text.isalpha())  # Output: True
```

### `isdigit()` - Returns `True` if all characters are digits
```python
text = "12345"
print(text.isdigit())  # Output: True
```

### `isalnum()` - Returns `True` if all characters are alphanumeric (letters or numbers)
```python
text = "Hello123"
print(text.isalnum())  # Output: True
```

### `isspace()` - Returns `True` if all characters are space
```python
text = "   "
print(text.isspace())  # Output: True
```

---


### `find(substring)` - Returns the index of the first occurrence of `substring`, or `-1` if not found
```python
text = "Python is amazing"
print(text.find("is"))  # Output: 7
```

### `replace(old, new)` - Replaces all occurrences of `old` with `new`
```python
text = "I love Python"
print(text.replace("love", "like"))  # Output: I like Python
```

---

---


### `strip()` - Removes leading and trailing spaces
```python
text = "   Hello World   "
print(text.strip())  # Output: "Hello World"
```

### `lstrip()` - Removes leading spaces
```python
text = "   Hello World"
print(text.lstrip())  # Output: "Hello World"
```

### `rstrip()` - Removes trailing spaces
```python
text = "Hello World   "
print(text.rstrip())  # Output: "Hello World"
```

---

## ⭐ **Why Use String Methods?**
✅ Improves Readability  
✅ Makes Text Manipulation Easier  
✅ Enhances Code Efficiency  
