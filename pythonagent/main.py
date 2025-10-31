import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    # Load environment variables from .env into process env (e.g., GEMINI_API_KEY, GEMINI_MODEL)
    load_dotenv()

    # Read required configuration from environment (.env file)
    api_key = os.environ.get("GEMINI_API_KEY")
    model = os.environ.get("GEMINI_MODEL")

    # Define and parse CLI arguments (optional positional prompt)
    parser = argparse.ArgumentParser(description="Generate content using Gemini API")
    parser.add_argument(
        "prompt",
        nargs="?",
        default="Write a very short story about a cat.",
        help="The prompt to send to the Gemini API (default: 'Write a very short story about a cat.')"
    )
    args = parser.parse_args()

    # Initialize Gemini client with API key
    client = genai.Client(api_key=api_key)

    # Build a structured content message as expected by google-genai types
    messages = [
        types.Content(role="user", parts=[types.Part(text=args.prompt)]),
    ]
    
    # Call the model with the chosen model name and the structured contents
    response = client.models.generate_content(
        model=model,
        contents=messages,
    )

    # Print the text output and basic token usage if available
    print(response.text)
    if response is not None or response.usage_metadata is not None:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print("No usage metadata found")

if __name__ == "__main__":
    main()