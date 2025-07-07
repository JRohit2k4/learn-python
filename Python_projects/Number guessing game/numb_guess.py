#using random module to get random number.
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_runninng = True

print("Welcome to number guessing game")
print(f"Guess a number between {lowest_num} to {highest_num}: ")

while is_runninng:
  guess = input("Enter your guess: ")

  if guess.isdigit():
    guess = int(guess)
    guesses +=1

    if guess < lowest_num or guess > highest_num:
      print("That nmber is out of the range!")
      print(f"Select a number between {lowest_num} to {highest_num}: ")
    elif guess < answer:
      print("Too low! Try again!")
    elif guess > answer:
      print("Too high! Try again!")

    else:
      print(f"CORRECT! The answer is {answer}")
      print(f"Number of guesses:{guesses}")
      is_runninng = False
