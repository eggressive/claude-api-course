# Load env variables from .env file
from dotenv import load_dotenv

load_dotenv()

from anthropic import Anthropic

# Initialize the Anthropic API client
client = Anthropic()
model = "claude-sonnet-4-5"

# Helper functions to handle the chat history
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

# Make a request to the API
def chat(messages, system=None, stop_sequences=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }

    if system:
        params["system"] = system

    if stop_sequences:
        params["stop_sequences"] = stop_sequences

    message = client.messages.create(**params)
    return message.content[0].text

messages = []

prompt = """Generate three different sample AWS CLI commands. Each should be very short."""

add_user_message(messages, prompt)

# Use message prefilling to guide the response format
# Add assistant message prefix to establish the pattern
add_assistant_message(messages, "```bash")

text = chat(messages, stop_sequences=["```"])
print(text.strip())
