from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def summarize_text(Input):

    client = genai.Client(api_key= api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction="""
            
            -> You are an Expert in Summarising the Article/Content.
            -> You are required to give summary to the Article/Content provided to you.
            -> Limit the response to 4 to 5 lines.
            
            
            """),
            contents= f'{Input}'
        )

    return response.text