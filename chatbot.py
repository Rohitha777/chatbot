print("Bot: Hello! I'm IntelliBot — your logic-based assistant.")
print("Bot: You can ask me simple things. Type 'exit' to end.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("IntelliBot: Session ended. Goodbye!")
        break

    elif user_input == "hi" or user_input == "hello":
        print("IntelliBot: Greetings. How can I assist you today?")

    elif user_input == "how are you":
        print("IntelliBot: I’m functioning within normal parameters. Thank you.")

    elif user_input == "what is your name":
        print("IntelliBot: I am IntelliBot, designed for structured conversation.")

    elif user_input == "what is ai":
        print("IntelliBot: AI stands for Artificial Intelligence — machines that simulate human thinking.")

    elif user_input == "what can you do":
        print("IntelliBot: I can respond to basic questions using rule-based logic.")

    elif user_input == "tell me a fact":
        print("IntelliBot: The first computer bug was an actual moth found in a machine in 1947.")

    elif user_input == "who created you":
        print("IntelliBot: I was created by a curious intern using Python and simple logic!")
    
    elif  user_input =="what is the time":
        from datetime import datetime
        print(f"IntelliBot: The current time is {datetime.now().strftime('%H:%M:%S')}.")


    elif user_input == "thank you":
        print("IntelliBot: You’re welcome. Always ready to help.")

    elif user_input == "":
        print("IntelliBot: Input not detected. Please type something.")

    else:
        print("IntelliBot: Sorry, I don't recognize that input. Try something else.")
