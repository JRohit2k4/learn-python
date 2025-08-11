import pyttsx3
import random
import time
import calendar

name = []
seconds = 1672215379.5045543 #seconds passed since epoch
local_time = time.ctime(seconds)

def quiz():
  questions = (
    "1. How many elements are in the periodic table?: ",
    "2. Which animal lays the largest egg?: ",
    "3. What is the most abundant gas in Earth's atmosphere?: ",
    "4. How many bones are in human body?: ",
    "5. Which planet in the solar system is the hottest?: ",
    "6. Who developed the theory of relativity?: ",
    "7. What is the capital city of Australia?: ",
    "8. Which ocean is the largest?: ",
    "9. Which programming language is known for its snake logo?: ",
    "10. What is the chemical symbol for gold?: "
  )

  options = (
      ("A. 118", "B. 119", "C. 122", "D. 121"),
      ("A. Whale", "B. Elephant", "C. Snake", "D. Ostrich"),
      ("A. Oxygen", "B. Hydrogen", "C. CO2", "D. Nitrogen"),
      ("A. 216", "B. 207", "C. 206", "D. 211"),
      ("A. Mars", "B. Mercury", "C. Venus", "D. Earth"),
      ("A. Isaac Newton", "B. Albert Einstein", "C. Nikola Tesla", "D. Galileo Galilei"),
      ("A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"),
      ("A. Indian Ocean", "B. Atlantic Ocean", "C. Arctic Ocean", "D. Pacific Ocean"),
      ("A. Java", "B. Python", "C. Ruby", "D. C++"),
      ("A. Au", "B. Ag", "C. Go", "D. Gd")
    )

  answers = ("A","D","D","C","C","B","C","D","B","A")


  running = True

  while running:

    guesses = []
    score = 0
    question_num = 0

    for question in questions:
      speak("This quiz will contain 10 questions.")
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


  
def casino_game():
    import random
    balance = 100
    speak("Welcome to the slot machine.")
    print("Welcome to Slot machine.")
    print("Symbols: 🍒 🔔 7️⃣ ⭐ ")

    def spin_row():
        symbols = ['🍒', '🔔', ' 7️⃣', '⭐']
        return [random.choice(symbols) for _ in range(3)]

    def print_row(row):
        print("|".join(row))
        #speak(" ".join(row))

    def get_payout(row, bet):
        if row[0] == row[1] == row[2]:
            if row[0] == '🍒':
                return bet * 3
            elif row[0] == '🔔':
                return bet * 5
            elif row[0] == '7️⃣':
                return bet * 8
            elif row[0] == '⭐':
                return bet * 10
        return 0

    while balance > 0:
        print(f"Current balance is Rs.{balance}")
        speak(f"Your current balance is {balance} rupees")

        bet = input("Enter your bet amount: ")
        speak("Enter your bet amount.")

        if not bet.isdigit():
            print("Please enter a valid number.")
            speak("Please enter a valid number.")
            continue
        
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds.")
            speak("Insufficient funds.")
            continue
            
        if bet <= 0:
            print("Bet must be greater than 0.")
            speak("Bet must be greater than zero.")
            continue 

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        speak("Spinning")
        time.sleep(1)
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won Rs.{payout}!")
            speak(f"You won {payout} rupees")
        else:
            print("Sorry! You lost this round.")
            speak("Sorry! You lost this round.")

        balance += payout

        if balance == 0:
            print("Sorry you are out of balance. Exiting game...")
            speak("Sorry you are out of balance. Exiting game.")
            break

        play_again = input("Wanna play again? (y/n): ").lower()
        speak("Wanna play again?")
        if play_again != 'y':
            print("Thanks for playing the slot machine!")
            speak("Thanks for playing the slot machine!")
            print("GAME OVER")
            print()
            break

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

    elif "casino" in user_input:
       casino_game()

    elif "bye" in user_input:
        response = "Goodbye! Have a great day!"
        print(f"Atom: {response}")
        speak(response)
        break
    else:
        response = "Sorry, I didn't understand that. Can you rephrase?"
        print(f"Atom: {response}")
        speak(response)
    
