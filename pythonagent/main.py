import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Write a story about a cat.",
)
print(response.text)
print(response.usage.model_tokens_details)
print(response.usage.prompt_tokens_details)
print(response.usage.completion_tokens_details)
print(response.usage.total_tokens_details)
print(response.usage.total_tokens)
print(response.usage.total_tokens_details)