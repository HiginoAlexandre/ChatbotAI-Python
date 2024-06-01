import sys
from configparser import ConfigParser
from Chatbot import ChatBot


def main():
    config = ConfigParser()
    try:
        config.read('credentials.ini')
        api_key = config['gemini_ai']['API_KEY']
    except (KeyError):
        print("Error: 'gemini_ai' section or 'API_KEY' missing in credentials.ini")
        sys.exit(1)  # Exit with an error code
    api_key = config['gemini_ai']['API_KEY']
    
    chatbot = ChatBot(api_key=api_key)
    chatbot.start_conversation()
    
    print("Welcome to the chatbot Ai (powered by the Gemini AI Language Model ). Type 'quit' to exit the chatbot")
    
    while True:
        user_input = input("You:  ")
        if user_input.lower() == 'quit':
            sys.exit("exiting chabot.....")
        
        try:
            response = chatbot.send_prompt(user_input)
            print(f"{chatbot.CHATBOT_NAME}: {response}")
        except Exception as e:
            print(f"Error : {e}")
            
            
main()
