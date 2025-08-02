import pyttsx3



def speak(text):
    engine = pyttsx3.init() # Initialize text-to-speech engine
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
        response = "I'm Python Bot, your friendly talking chatbot!"
        print(f"Atom: {response}")
        speak(response)
    
    elif "bye" in user_input:
        response = "Goodbye! Have a great day!"
        speak(response)
        print(f"Atom: {response}")
        break
    else:
        response = "Sorry, I didn't understand that. Can you rephrase?"
    
print(f"🤖 Chatbot: {response}")
speak(response)
