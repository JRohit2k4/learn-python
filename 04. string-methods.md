# Python String Methods

Python provides several built-in methods to manipulate strings. Below is a list of commonly used string methods with examples.

---

## 1️⃣ **Changing Case**

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

## 2️⃣ **Checking String Content**

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

### `isspace()` - Returns `True` if all characters are whitespace
```python
text = "   "
print(text.isspace())  # Output: True
```

---

## 3️⃣ **Finding and Replacing**

### `find(substring)` - Returns the index of the first occurrence of `substring`, or `-1` if not found
```python
text = "hello world"
print(text.find("o"))  # Output: 4
```

### `rfind(substring)` - Returns the index of the last occurrence of `substring`, or `-1` if not found
```python
text = "hello world hello"
print(text.rfind("hello"))  # Output: 12
```

### `replace(old, new)` - Replaces all occurrences of `old` with `new`
```python
text = "I love Python"
print(text.replace("love", "like"))  # Output: I like Python
```

---

## 4️⃣ **String Length**

### `len(string)` - Returns the length of the string
```python
text = "hello world"
print(len(text))  # Output: 11
```

---

## 5️⃣ **Splitting and Joining Strings**

### `split(separator)` - Splits the string into a list based on the separator
```python
text = "apple,banana,cherry"
print(text.split(","))  # Output: ['apple', 'banana', 'cherry']
```

### `join(iterable)` - Joins elements of an iterable into a string with a separator
```python
words = ["hello", "world"]
print(" ".join(words))  # Output: hello world
```

---

## 6️⃣ **Stripping Whitespaces**

### `strip()` - Removes leading and trailing spaces
```python
text = "   hello world   "
print(text.strip())  # Output: "hello world"
```

### `lstrip()` - Removes leading spaces
```python
text = "   hello world"
print(text.lstrip())  # Output: "hello world"
```

### `rstrip()` - Removes trailing spaces
```python
text = "hello world   "
print(text.rstrip())  # Output: "hello world"
```

---

## ⭐ **Why Use String Methods?**
✅ Improves Readability  
✅ Makes Text Manipulation Easier  
✅ Enhances Code Efficiency  

