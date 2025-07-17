balance = 0

def show_balance():
  print(f"Your current balance is {balance:.2f} Rs.")

def deposit():
  amount = float(input("Enter your deposit amount: "))

  if amount < 0:
    print("That's not a valid amount!")
  else:
    print(f"Rs.{amount} has been deposited.")
    return amount

def withdraw():
  amount = float(input("Enter your withdraw amount: "))

  if amount > balance:
    print("Insufficient funds!")
  elif amount < 0:
    print("Value shoud be greater than 0")
  else:
    return amount

is_running = True

while is_running:
  print()
  print("------- Banking Program -------")
  print()
  print("1.Show your Balance")
  print("2.Deposit")
  print("3.Withdraw")
  print("4.Exit")
  print()
  print("-------------------------------")

  choice = input("Enter your choice: ")

  if choice == "1":
    show_balance()
  elif choice == "2":
     balance += deposit()
  elif choice == "3":
     balance -= withdraw()
  elif choice == "4":
     is_running = False
  else: 
     print("Invalid choice!!")

print("Thank you! Have a nice day.")
print()
