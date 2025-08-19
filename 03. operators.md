# Operators in Python

Operators in Python are special symbols that perform operations on variables and values. Python supports various types of operators, which are categorized as follows:

## 1. Arithmetic Operators  
These operators are used to perform mathematical calculations.

| Operator | Symbol | Example | Result |
|----------|--------|---------|--------|
| Addition | `+` | `5 + 3` | `8` |
| Subtraction | `-` | `5 - 3` | `2` |
| Multiplication | `*` | `5 * 3` | `15` |
| Division | `/` | `5 / 2` | `2.5` |
| Floor Division | `//` | `5 // 2` | `2` |
| Modulus | `%` | `5 % 2` | `1` |
| Exponentiation | `**` | `5 ** 2` | `25` |

### Example:
```python
x = 10
y = 3
print(x + y)  # Output: 13
print(x - y)  # Output: 7
print(x * y)  # Output: 30
print(x / y)  # Output: 3.33
```

## 2. Comparison Operators  
These operators compare values and return a Boolean result (True or False).

| Operator | Symbol | Example | Result |
|----------|--------|---------|--------|
| Equal to | `==` | `5 == 3` | `False` |
| Not equal to | `!=` | `5 != 3` | `True` |
| Greater than | `>` | `5 > 3` | `True` |
| Less than | `<` | `5 < 3` | `False` |
| Greater than or equal to | `>=` | `5 >= 3` | `True` |
| Less than or equal to | `<=` | `5 <= 3` | `False` |

### Example:
```python
a = 10
b = 5
print(a > b)  # Output: True
print(a == b) # Output: False
print(a != b) # Output: True
```

## 3. Logical Operators  
Logical operators are used to combine conditional statements.

| Operator | Symbol | Example | Result |
|----------|--------|---------|--------|
| AND | `and` | `True and False` | `False` |
| OR | `or` | `True or False` | `True` |
| NOT | `not` | `not True` | `False` |

### Example:
```python
x = True
y = False
print(x and y)  # Output: False
print(x or y)   # Output: True
print(not x)    # Output: False
```

## 4. Bitwise Operators  
These operators perform bit-level operations.

| Operator | Symbol | Example | Result (Binary) |
|----------|--------|---------|----------------|
| AND | `&` | `5 & 3` | `1` (0101 & 0011 = 0001) |
| OR | `|` | `5 | 3` | `7` (0101 | 0011 = 0111) |
| XOR | `^` | `5 ^ 3` | `6` (0101 ^ 0011 = 0110) |
| NOT | `~` | `~5` | `-6` (Inverts bits) |
| Left Shift | `<<` | `5 << 1` | `10` (0101 → 1010) |
| Right Shift | `>>` | `5 >> 1` | `2` (0101 → 0010) |

### Example:
```python
a = 5  # 0101
b = 3  # 0011
print(a & b)  # Output: 1
print(a | b)  # Output: 7
print(a ^ b)  # Output: 6
```

## 5. Assignment Operators  
These operators assign values to variables.

| Operator | Symbol | Example | Equivalent To |
|----------|--------|---------|--------------|
| Assign | `=` | `x = 5` | `x = 5` |
| Add and Assign | `+=` | `x += 3` | `x = x + 3` |
| Subtract and Assign | `-=` | `x -= 3` | `x = x - 3` |
| Multiply and Assign | `*=` | `x *= 3` | `x = x * 3` |
| Divide and Assign | `/=` | `x /= 3` | `x = x / 3` |

### Example:
```python
x = 10
x += 5  # x = x + 5
print(x)  # Output: 15
```

---

This covers all the major operators in Python. 🚀 Let me know if you want any modifications! 😊

