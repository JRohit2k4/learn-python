menu = {"Pizza":200,
        "Burger":150,
        "Popcorn":500,
        "Tacos":100,
        "Frankie":100,
        "Coke":50}

cart = []
total = 0



print("--------- MENU ---------")
for key, value in menu.items():
  print(f"{key:10}: Rs.{value:.2f}")
print("------------------------")

while True:
  food = input("Select an item (q for quit): ").capitalize()
  if food == "Q":
    break
  elif menu.get(food) is not None:
    cart.append(food)
  else:
    print(f"Sorry! {food} is not available.")
print()

if not cart:
  print("You didn't ordered anything.")
  print()
else:
  print("------ YOUR ORDER ------")
  for food in cart:
    price = menu[food]
    total += menu.get(food)
    print(f"{food.capitalize():10}:Rs.{price:.2f} ")

  print("------------------------")
  print(f"Your total is Rs.{total:.2f}")
  print()
