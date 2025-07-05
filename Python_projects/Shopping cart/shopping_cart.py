# Shopping cart system

foods = []  #using list because it is changeable
prices = []
total = 0

while True:
  food = input("Enter your food(q to quit): ")
  if food.lower() == "q":
    break
  else:
    price = float(input(f"Enter price of {food}: Rs. "))
    foods.append(food)
    prices.append(price)

print("----- YOUR CART -----")

for food in foods:
  print(food)

for price in prices:
  total += price

print("---------------------")
print(f"Your total is Rs. {total}")
