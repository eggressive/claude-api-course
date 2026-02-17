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
def chat(messages, system=None, temperature=0.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text

# Start with an empty message list
messages = []

# Add the initial user question
add_user_message(messages, "Is tea or coffee better at breakfast?")

# Add assistant message to the message list
add_assistant_message(messages, "Coffee is very good because")

# Get Claude's response
answer = chat(messages)
print(f"Claude: {answer}\n")
