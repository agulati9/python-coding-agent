# Standard library imports
import os  # For accessing environment variables
import argparse  # For parsing command-line arguments

# Third-party imports
from dotenv import load_dotenv  # For loading .env file variables
from google import genai  # Google's Gemini AI client
from google.genai import types  # Types for structuring messages
from functions.get_files_info import get_files_info

def main():
    """
    Main function that orchestrates the Gemini API interaction:
    1. Loads environment variables
    2. Parses command-line arguments
    3. Initializes the Gemini client
    4. Makes an API request
    5. Displays the response
    """
    
    # Load environment variables from .env file into the process environment
    # This reads variables like GEMINI_API_KEY and GEMINI_MODEL from your .env file
    load_dotenv()

    # Retrieve required configuration from environment variables
    # These are read from the .env file that was loaded above
    api_key = os.environ.get("GEMINI_API_KEY")  # Your Gemini API key
    model = os.environ.get("GEMINI_MODEL")  # The model name to use (e.g., "gemini-2.0-flash")

    # Set up command-line argument parser
    # This allows users to pass a prompt as an argument when running the script
    parser = argparse.ArgumentParser(description="Generate content using Gemini API")
    
    # Add a positional argument for the prompt (optional, has a default value)
    # nargs="?" means the argument is optional
    parser.add_argument(
        "prompt",
        nargs="?",
        default="Write a very short story about a cat.",
        help="The prompt to send to the Gemini API (default: 'Write a very short story about a cat.')"
    )
    
    # Add a flag for verbose output (optional, defaults to False if not provided)
    # action="store_true" means the flag is True if present, False otherwise
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print verbose output including token usage and model information"
    )
    
    # Parse the command-line arguments and store them in args
    args = parser.parse_args()

    # Initialize the Gemini API client with your API key
    # This creates a client object that will be used to make API calls
    client = genai.Client(api_key=api_key)

    # Structure the message content in the format expected by the API
    # The API expects messages as a list of Content objects with role and parts
    messages = [
        types.Content(role="user", parts=[types.Part(text=args.prompt)]),
    ]
    
    # Make the API call to generate content
    # This sends your prompt to the Gemini model and waits for a response
    response = client.models.generate_content(
        model=model,  # The model to use (from environment variable)
        contents=messages,  # The structured message content
    )

    # Display the response text (this is always shown)
    # print(response.text)
    
    # Handle verbose output and usage metadata
    # Check if we have a valid response with usage metadata
    # if response is not None or response.usage_metadata is not None:
    #     # Only show verbose details if the --verbose flag was used
    #     if args.verbose:
    #         print(f"Using model: {model}")
    #         print(f"Using API key: {api_key}")
    #         print(f"Using prompt: {args.prompt}")
    #         print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    #         print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    # else:
    #     print("No usage metadata found")

    print(get_files_info("calculator"))

if __name__ == "__main__":
    main()  