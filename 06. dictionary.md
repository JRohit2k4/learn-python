## Dictionary: A collection of {key:value} pairs.

**Dictionary** in Python is:

✅ Ordered (the order of elements is maintained)  
✅ Changeable (you can update, add, or remove items)  
✖️: NO duplicates   

📍 Example:
```python
capitals = {"India":"New Delhi",
            "USA":"Washington D.C.",
            "Japan":"Tokyo",
            "China":"Beijing",
            "Russia":"Moscow"}
```
| Method                          | Description                                    |
| ------------------------------- | ---------------------------------------------- |
| `print(capitals.get("India"))`              | Gets the value of India i.e New Delhi   |
| `capitals.update({"USA":"Detroit"})`        | Updates the value of USA                |
| `capitals.update({"Australia":"Sydney"})`   | Adds the new pair                       |
| `capitals.pop("China")`                     | Removes the pair China                  |
| `capitals.popitem()`                        | Removes the last pair                   |
| `capitals.clear()`                          | Clears the dictionary                   |

````

capitals = {"India":"New Delhi",
            "USA":"Washington D.C.",
            "Japan":"Tokyo",
            "China":"Beijing",
            "Russia":"Moscow"}  

# Gets the value of India
print(capitals.get("India"))         
# New Delhi

# Updates the value of USA
capitals.update({"USA":"Detroit"})

# Adds the new pair
capitals.update({"Australia":"Sydney"})

# Removes the pair China
capitals.pop("China")           

# Removes the last pair
capitals.popitem()         

# Clears the dictionary
capitals.clear()         

