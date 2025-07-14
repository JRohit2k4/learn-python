## Membership operators
used to test hether a value or variable is found in the sequence(string, list, set, tuple, or dictionary)


**1. in**  
```python
students = {"Spongebob", "Patric", "Sandy"}
student = input("Enter the name of student: ")

if student in students:
  print(f"{student} is a student")
else:
  print(f"{student} was not found")
```

**2. not in**
```python
students = {"Spongebob", "Patric", "Sandy"}
student = input("Enter the name of student: ")

if student not in students:
  print(f"{student} was not found")
else:
  print(f"{student} is a student")
```
