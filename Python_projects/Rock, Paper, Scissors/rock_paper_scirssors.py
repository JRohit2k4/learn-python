import random

options = ("rock","paper","scissors")

player = None
computer = random.choice(options)

while player not in options:
 player = input("Throw your weapon: ")


print(f"Player: {player}")
print(f"Computer: {computer}")


if player == computer:
 print("It's a tie!!")
elif player == "rock" and computer == "scissors":
 print("You WIN!!")
elif player == "paper" and computer == "rock":
 print("You WIN!!")
elif computer == "scissors" and player == "paper":
 print("You WIN!!")
else:
 print("You LOOSE!!")
