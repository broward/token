import openai

# Initialize the OpenAI client with your API key
# Open States API Key
file = open('/home/gypsy/Project/keys/openai_api_key.json', "r")
API_KEY = file.read().strip()
print(API_KEY)
file.close()


# Set your OpenAI API key
openai.api_key = API_KEY

from pathlib import Path
from openai import OpenAI

client = OpenAI()

client.files.create(
    file=Path("venv.sh"),
    purpose="fine-tune",
)
