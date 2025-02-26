#taking input from user
num = int(input("Enter a number: "))

#initializing the factorial result
factorial = 1

#checking if the number is Negative, Positive or Zero
if num < 0:
  print("Enter positive number.")
elif num == 0:
  print("No zero's allowed..")
else:
  #calculate factorial
  for i in range(1,num + 1):
    factorial *=i #multiplying numbers from 1 to num
  print(f"Factorial of {num} is {factorial}")
