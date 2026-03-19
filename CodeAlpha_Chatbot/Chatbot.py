def chatbot():
    """
    A simple rule-based chatbot that responds to basic user inputs
    """
    
    # Define response rules
    def get_response(user_input):
        # Convert input to lowercase for easier matching
        user_input = user_input.lower().strip()
        
        # Greetings
        if user_input in ["hello", "hi", "hey", "greetings"]:
            return "Hi there! How can I help you today?"
        
        elif user_input in ["how are you", "how r u", "how are you doing"]:
            return "I'm doing great, thanks for asking! How about you?"
        
        # Feelings responses
        elif "good" in user_input or "great" in user_input:
            return "That's wonderful to hear!"
        
        elif "bad" in user_input or "sad" in user_input:
            return "I'm sorry to hear that. Hope things get better!"
        
        # Time queries
        elif "time" in user_input:
            import datetime
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}"
        
        # Name queries
        elif "your name" in user_input:
            return "My name is ChatBot! I'm your virtual assistant."
        
        elif "my name" in user_input:
            return "I don't know your name yet. What is it?"
        
        # Capabilities
        elif "what can you do" in user_input or "help" in user_input:
            return """I can respond to basic greetings, tell you the time, 
and have simple conversations. Try saying hello or asking about my name!"""
        
        # Jokes
        elif "joke" in user_input:
            return "Why don't scientists trust atoms? Because they make up everything! 😄"
        
        # Farewell
        elif user_input in ["bye", "goodbye", "exit", "quit"]:
            return "Goodbye! Have a great day!"
        
        # Default response for unrecognized input
        else:
            return "I'm not sure how to respond to that. Try saying 'hello' or 'help'!"
    
    # Welcome message
    print("=" * 50)
    print("Welcome to Simple ChatBot!".center(50))
    print("=" * 50)
    print("Type 'bye' to exit the conversation\n")
    
    # Main conversation loop
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        # Check if user wants to exit
        if user_message.lower() in ["bye", "goodbye", "exit", "quit"]:
            print(f"Bot: {get_response(user_message)}")
            break
        
        # Get and display bot response
        bot_response = get_response(user_message)
        print(f"Bot: {bot_response}")
    
    print("\nThanks for chatting! See you next time!")

# Run the chatbot
if __name__ == "__main__":
    chatbot()