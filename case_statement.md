## Match-case statement (switch):

An alternative to using 'elif' statements.  
Execute some code if a value matches a 'case'.  
Benefits: cleaner and syntax is more readable.  

**Checking the day of week:**
```python
def day_of_week(day)
  match day:
    case 1:
      return "It is Sunday "
    case 2:
      return "It is Monday "
    case 3:
      return "It is Tuesday "
    case 4:
      return "It is Wednesday "
    case 5:
      return "It is Thursday "
    case 6:
      return "It is Friday "
    case 7:
      return "It is Saturday "
    case _:
      return "Invalid day"
print(day_of_week(1))
```

**Checking is it a weekend:**
```python
def is_weekend(day)
  match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
      return False
    case :
      return True
    case _:
      return False

print(day_of_week("Monday"))
```
