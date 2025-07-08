import random

options = ("rock","paper","scissors")

player = None
computer = random.choice(options)

running = True

while running:

  player = None
  computer = random.choice(options)
  while player not in options:
   player = input("Throw your weapon (rock/paper/scissors): ")


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
    print("You LOSE!!")

  play_again = input("Wanna play again (y/n): ")
  if not play_again == "y":
    running = False

print("Thanks for playing!")


 
