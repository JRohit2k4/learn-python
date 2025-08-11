import pyttsx3
import random
import time
import calendar

name = []
seconds = 1672215379.5045543 #seconds passed since epoch
local_time = time.ctime(seconds)

def quiz():
  questions = ("1. How many elements are in the periodic table?: ",
              "2. Which animal lays the largest egg?: ",
              "3. What is the most abundant gas in Earth's atmosphere?: ",
              "4. How many bones are in human body?: ",
              "5. Which planet in the solar system is the hottest?: ")

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
      print(" STARTING QUIZ GAME ")
      print("--------------------")
      print(question)
      speak(question)
      for option in options[question_num]:
        print(option)
        speak(option)

      guess = input("Enter options (A/B/C/D): ").upper()
      guesses.append(guess) 
      if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
        speak("CORRECT!")
      else:
        print("INCORECT!")
        speak("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer.")
        speak(f"{answers[question_num]} is the correct answer.")
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
    speak(f"Your score is: {score}%")
    print()

    if score < 100:
      choice = input("Wanna to play again? (y/n): ").lower()
      speak("Wanna to play again?")
      if choice != "y":
          running = False
    else:
        print("Perfect score!  You crushed it! Game over.")
        speak("Perfect score!  You crushed it! Game over.")
        running = False
        print()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

print("Atom: Hello! My name is Atom. I'm your talking chatbot. (Type 'bye' to exit)")
speak("Hello! My name is Atom. I'm your talking chatbot.")


while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print(f"Atom: Hello there! How can I help you?")
        speak("Hello there! How can I help you?")
    
    elif "how are you" in user_input:
        response = "I'm just a bot, but I'm doing great! How about you?"
        print(f"Atom: {response}")
        speak(response)
    
    elif "your name" in user_input:
        response = "My name is Atom. What's your?"
        print(f"Atom: {response}")
        speak(response)
        name = input("What's your name?: ")
        print(f"Hello {name}! Nice to see you. (I can see you through camera.)")
        speak(f"Hello {name}! Nice to see you.")
          
    elif user_input in ["what are you", "tell me about yourself", "info", "who are you"]:
        response = "My name is Atom. I'm a simple chatbot created by Rohit on August 2nd 2025. I can do math, tell you some dad jokes, and play quiz. Currently I'm in my beta version, so might have some errors or patches, but don't worry I will inform that to Rohit(My creator). That's all about myself"
        print(f"Atom: {response}")
        speak(response)
    
    elif user_input in ["bored", "im bored", "what can you do"]:
        response = "What would you like me to do? I can do math, tell you jokes, riddles and play quiz or do you wanna play casino?."
        print(f"Atom: {response}")
        speak(response)

    elif user_input in ["what is time", "time", "date"]:
       response = f"Current time is {local_time}"
       print(f"{local_time}")
       speak(response)

    elif "quiz" in user_input:
       quiz()

    elif "bye" in user_input:
        response = "Goodbye! Have a great day!"
        print(f"Atom: {response}")
        speak(response)
        break
    else:
        response = "Sorry, I didn't understand that. Can you rephrase?"
        print(f"Atom: {response}")
        speak(response)
    
