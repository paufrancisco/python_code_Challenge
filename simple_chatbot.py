import nltk
from nltk.chat.util import Chat, reflections

# Define a set of patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello! How can I assist you today?"]),
    (r"what is your name?", ["I am a chatbot created to assist you."]),
    (r"how are you?", ["I'm doing well, thank you! How can I help you?"]),
    (r"what can you do?", ["I can answer simple questions and chat with you."]),
    (r"bye|exit", ["Goodbye! Have a great day!"]),
    (r"(.*)", ["I'm sorry, I didn't understand that."])
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()
