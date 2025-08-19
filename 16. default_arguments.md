## default arguments 
Adefault value for certain parameters default is used when the argument is omitted makes your function more flexible, reduces number of parameters.

```python
def net_price(list_price, distount=0.1, tax=0.05)
  return list_price * (1- discount) * (1+tax)

print(net_price(500))
```
