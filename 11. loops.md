# Loops in Python

Loops in Python allow us to execute a block of code multiple times. Python provides two types of loops:

1. **For Loop** - Iterates over a sequence (list, tuple, dictionary, string, etc.).
2. **While Loop** - Executes as long as a condition is `True`.

## 1. For Loop
The `for` loop is used to iterate over a sequence.

### Syntax:
```python
for variable in sequence:
    # Code block to execute
```

### Example:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
**Output:**
```
apple
banana
cherry
```

### Using `range()` in For Loop:
```python
for i in range(5):
    print(i)
```
**Output:**
```
0
1
2
3
4
```

---

## 2. While Loop
The `while` loop continues execution until the condition becomes `False`.

### Syntax:
```python
while condition:
    # Code block to execute
```

### Example:
```python
x = 0
while x < 5:
    print(x)
    x += 1
```
**Output:**
```
0
1
2
3
4
```

---

## 3. Loop Control Statements
Python provides special statements to control loop execution:

| Statement | Description | Example |
|-----------|------------|---------|
| `break` | Exits the loop completely | `if x == 3: break` |
| `continue` | Skips the current iteration and continues | `if x == 3: continue` |
| `pass` | Does nothing (used as a placeholder) | `if x == 3: pass` |

### Example:
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```
**Output:**
```
0
1
2
```

```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```
**Output:**
```
0
1
2
4
```

---
