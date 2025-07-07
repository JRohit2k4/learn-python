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
