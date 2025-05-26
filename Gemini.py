
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()
api_key = os.getenv("API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works in a few words",
)

print(response)
