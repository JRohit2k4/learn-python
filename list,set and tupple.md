## 1. List

**List** in Python is:
- ✅ Ordered (the order of elements is maintained)
- ✅ Changeable (you can update, add, or remove items)
- ✅ Allows duplicates

---

## 📍 Example:
```python
fruits = ["apple", "banana", "orange", "mango"]

| Method                          | Description                                      |
| ------------------------------- | ------------------------------------------------ |
| `fruits.append("pineapple")`    | Adds "pineapple" to the end of the list          |
| `fruits.remove("mango")`        | Removes "mango" from the list                    |
| `fruits.insert(0, "pineapple")` | Inserts "pineapple" at index `0`                 |
| `fruits.sort()`                 | Sorts the list in alphabetical (ascending) order |
| `fruits.reverse()`              | Reverses the order of the list                   |
| `fruits.clear()`                | Removes all elements from the list               |
| `print(fruits.index(mango))`    | Prints the index number of mango in the list     | 
| `print(fruits.count(banana))`   | Prints how many bananas are there                |

fruits = ["apple", "banana", "orange", "mango"]

# Add pineapple to the end
fruits.append("pineapple")         
# ["apple", "banana", "orange", "mango", "pineapple"]

# Remove mango
fruits.remove("mango")             
# ["apple", "banana", "orange", "pineapple"]

# Insert pineapple at the beginning
fruits.insert(0, "pineapple")      
# ["pineapple", "apple", "banana", "orange", "pineapple"]

# Sort list alphabetically
fruits.sort()                      
# ['apple', 'banana', 'orange', 'pineapple', 'pineapple']

# Reverse the sorted list
fruits.reverse()                   
# ['pineapple', 'pineapple', 'orange', 'banana', 'apple']

# Clear all elements from the list
fruits.clear()                     
# []

# Prints the index number of an element in the list
print(fruits.index(mango))
# 3

# Prints the index number of mango in the list
print(fruits.count(banana))
# 1

```


## 2. Set

**Set** in Python is:
- ✅ Unordered
- ✅ Changeable (you can update, add, or remove items)
- ✅ NO duplicates

---

## 📍 Example:
```python
fruits = {"apple", "banana", "orange", "mango"}

| Method                          | Description                                      |
| ------------------------------- | ------------------------------------------------ |
| `fruits.add("pineapple")`       | Adds "pineapple" to the set                      |
| `fruits.remove("mango")`        | Removes "mango" from the set                     |
| `fruits.pop()`                  | Removes first(random) element from the set       |
| `fruits.clear()`                | Removes all elements from the list               | 

fruits = {"apple", "banana", "orange", "mango"}

# Add pineapple to the end
fruits.add("pineapple")         
# {"apple", "banana", "orange", "mango", "pineapple"}

# Remove mango
fruits.remove("mango")             
# {"apple", "banana", "orange", "pineapple"}

# Removes first(random) element from the set
fruits.pop()      
# {"apple", "banana", "orange", "pineapple"}

# Clear all elements from the list
fruits.clear()
# {}                    

```
