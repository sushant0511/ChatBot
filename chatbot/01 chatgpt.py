import os
import logging
from dotenv import load_dotenv
import openai

# Import the logger from the main module
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv("../.env")

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

# Send prompt to OpenAI Chat API
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with OpenAI APIs"}]
)

# Print the response
print(completion.choices[0].message.content)