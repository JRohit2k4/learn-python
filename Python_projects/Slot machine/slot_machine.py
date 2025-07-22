import random

def spin_row():
  symbols = ("⭐","🍒","🔔")
  return[random.choice(symbols) for symbol in range(3)] #used list comprehension to shorten the code

def print_row(row):
  print("********************")
  print(" | ".join(row))
  print("********************")


def get_payout(row, bet):
  if row[0] == row[1] == row[2]
    if row[0] == '🍒':
      return bet * 2
    if row[0] == '🔔':
      return bet * 5
    if row[0] == '⭐':
      return bet * 10
  return 0

balance = 100

print("********************")
print("Python slot machine ")
print("Symbols: 🍒  🔔  ⭐")
print("********************")

while balance > 0:
  print(f"Currrent balance is Rs.{balance}")

  bet = input("Enter bet amount")

  if not bet.isdigit():
    print("Please enter a valid number")
    continue

  bet = int(bet)
  
  if bet > balance:
    print("Insufficient funds")
    continue
  
  if bet <= 0:
    print("Bet must be greater than 0")
    continue

  balance -= bet
  
  row = spin_row
  print("Spinning...\n")
  print_row(row)

  payout = get_payout(row, bet)
  if payout > 0:
    print(f"You won Rs.{payout}")
  else:
    print("Sorry! Try again.")

  balance += payout
  
