import os
import argparse
from dotenv import load_dotenv

def main():
    parser = argparse.ArgumentParser(description="Generate content using Gemini API")
    parser.add_argument(
        "prompt",
        nargs="?",
        default="Write a very short story about a cat.",
        help="The prompt to send to the Gemini API (default: 'Write a very short story about a cat.')"
    )
    args = parser.parse_args()
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    from google import genai

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=args.prompt,
    )
    print(response.text)
    if response is not None or response.usage_metadata is not None:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print("No usage metadata found")

if __name__ == "__main__":
    main()