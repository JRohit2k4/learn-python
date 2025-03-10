def chatbot():
    print("Hello! I am a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello"]:
            print("Bot: Hello! How can I help you?")
        elif user_input in ["how are you?", "how's it going?"]:
            print("Bot: I'm just a bot, but I'm doing great!")
        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day.")
        #We can add more communication using elif blocks.
            break
        else:
            print("Bot: I'm not sure how to respond to that.")

chatbot()

