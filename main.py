import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    model = "gemini-2.0-flash-001"
    #prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    client = genai.Client(api_key=api_key)
    
    if len(sys.argv) == 0:
        sys.exit(1)
    user_prompt = sys.argv[1]
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    response = client.models.generate_content(
        model=model, contents=messages
    )
    
    print(response.text)
    prompt_tokens = response.usage_metadata.prompt_token_count
    resp_tokens = response.usage_metadata.candidates_token_count
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: ")



if __name__ == "__main__":
    main()