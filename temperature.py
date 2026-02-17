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
def chat(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text

# Start with an empty message list
messages = []

# System prompt to set the context for the tutor
# system = """
# You are a patient math tutor.
# Do not directly answer a student's questions.
# Guide them to a solution step by step.
# """

# Add the initial user question
add_user_message(messages, "Generate a one sentence movie idea.")

# Get Claude's response
# answer = chat(messages, system=system)
answer = chat(messages, temperature=1.0)
print(f"Claude: {answer}\n")
