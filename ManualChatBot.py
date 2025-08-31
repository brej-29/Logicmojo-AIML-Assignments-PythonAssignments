import random
import datetime

def start_chat():
    user_name = greet_and_get_name()
    print("\nLet's start chatting! (type 'bye' to exit)")

    while True:
        user_input = input(f"{user_name}: ")
        bot_response = get_bot_response(user_input, user_name)
        print(f"Bot: {bot_response}")

        # Check for exit condition
        farewells = ["bye", "goodbye", "quit", "exit"]
        if any(word in user_input.lower() for word in farewells):
            break

    print("\nThank you for chatting with me!")

def greet_and_get_name():
    print("Hello! I am a simple chatbot. I'm here to chat with you.")
    print("You can ask me some simple questions, and I'll do my best to answer.")
    print("Type 'bye' or 'quit' to exit.\n")
    
    name_prompts = [
        "First, what should I call you? ",
        "Before we start, what's your name? ",
        "I'd love to know your name: "
    ]
    
    name = input(random.choice(name_prompts))
    print(f"\nNice to meet you, {name}!")
    return name

def get_bot_response(user_input, user_name):
    processed_input = user_input.lower().strip()

    greetings = ["hello", "hi", "hey", "greetings", "howdy"]
    if any(word in processed_input for word in greetings):
        responses = [
            f"Hello there, {user_name}!",
            f"Hi, {user_name}! How can I help you today?",
            f"Hey, {user_name}! Great to see you."
        ]
        return random.choice(responses)

    farewells = ["bye", "goodbye", "quit", "exit", "see you"]
    if any(word in processed_input for word in farewells):
        responses = [
            f"Goodbye, {user_name}! Have a great day!",
            f"See you later, {user_name}!",
            f"Bye, {user_name}! Come back soon."
        ]
        return random.choice(responses)

    if "how are you" in processed_input:
        responses = [
            "I'm just a bunch of code, but I'm doing great! Thanks for asking.",
            "I'm functioning as expected. How about you?",
            "I'm doing well, thank you! Ready to help."
        ]
        return random.choice(responses)

    if any(word in processed_input for word in ["your name", "name"]):
        responses = [
            "You can call me Brejesh Assist Chatbot.",
            "I'm your friendly neighborhood chatbot!",
            "I don't have a name, but I'm here to help you."
        ]
        return random.choice(responses)
    
    if any(word in processed_input for word in ["what can you do", "can you do", "help"]):
        return (
            "I can do a few things! You can greet me, ask me how I am, "
            "ask for my name, or ask for the current time. "
            "Just type 'bye' to end our chat."
        )

    if "time" in processed_input:
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        return f"The current time is {current_time}."

    if "thank you" in processed_input or "thanks" in processed_input:
        responses = [
            "You're welcome!",
            "No problem at all!",
            f"Anytime, {user_name}!"
        ]
        return random.choice(responses)

    fallback_responses = [
        "I'm not sure how to respond to that. Can you try asking something else?",
        "That's an interesting question! I don't have an answer for it yet.",
        "I'm still learning. Could you rephrase that?",
        f"Sorry, {user_name}, I don't understand that. You can type 'help' to see what I can do."
    ]
    return random.choice(fallback_responses)

start_chat()