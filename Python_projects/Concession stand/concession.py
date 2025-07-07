menu = {"pizza":200,
        "burger":150,
        "popcorn":500,
        "tacos":100,
        "frankie":100,
        "coke":50}

cart = []
total = 0



print("--------- MENU ---------")
for key, value in menu.items():
  print(f"{key:10}: Rs.{value:.2f}")
print("------------------------")

while True:
  food = input("Select an item (q for quit): ").lower()
  if food == "q":
    break
  elif menu.get(food) is not None:
    cart.append(food)

print("------ YOUR ORDER ------")
for food in cart:
  total += menu.get(food)
  print(food)

print("------------------------")
print(f"Your total is Rs.{total:.2f}")
print()
