import random

questions = ("1.How many elements are in the periodic table?: ",
             "2.Which animal lays the largest egg?: ",
             "3.What is the most abundant gas in Earth's atmosphere?: ",
             "4.How many banes are in human body?: ",
             "5.Which planet in the solar system is the hottest?: ")

options = (("A. 118", "B. 119", "C. 122", "D. 121"),
           ("A. Whale", "B. Elephant", "C. Snake", "D. Ostrich"),
           ("A. Oxygen", "B. Hydrogen", "C. CO2", "D. Nitrogen"),
           ("A. 216", "B. 207", "C. 206", "D. 211"),
           ("A. Mars", "B. Mercury", "C. Venus", "D. Earth"))

answers = ("A","D","D","C","C")



running = True

while running:

  guesses = []
  score = 0
  question_num = 0

  for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
      print(option)

    guess = input("Enter options (A/B/C/D): ").upper()
    guesses.append(guess) 
    if guess == answers[question_num]:
      score += 1
      print("CORRECT!")
    else:
      print("INCORECT!")
      print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

  print("--------------------")
  print("       RESULT       ")
  print("--------------------")


  print("Answers: ",end=" ")
  for answer in answers:
    print(answer,end= " ")
  print()

  print("Guesses: ",end=" ")
  for guess in guesses:
    print(guess,end= " ")
  print()

  score = int(score / len(questions) * 100)
  print(f"Your score is: {score}%")
  print()

  if score < 100:
    choice = input("Wanna to play again? (y/n): ").lower()
    if choice != "y":
        running = False
  else:
      print("Perfect score! Game over. You crushed it!")
      running = False
      print()
