from anthropic import Anthropic

# Load env variables from .env file
from dotenv import load_dotenv

load_dotenv()

# Initialize the Anthropic API client
client = Anthropic()
model = "claude-sonnet-4-5"  # Specify the model you want to use  

# Helper functions to handle the chat history
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

# Make a request to the API
def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text

# Start with an empty message list
messages = []

# Interactive chatbot loop
print("Chatbot started! Type 'exit' to quit.\n")

while True:
    # Prompt the user to enter some input
    user_input = input("You: ")

    # Exit if user types 'exit'
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Add user input to the message list
    add_user_message(messages, user_input)

    # Call the API
    response = chat(messages)

    # Add Claude's response to the message list
    add_assistant_message(messages, response)

    # Print the generated text
    print(f"Claude: {response}\n")
