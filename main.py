import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from call_function import available_functions,call_function
from prompts.prompts import SystemPrompts
# load llm
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
# integrate with gemini llm obj instance
client = genai.Client(api_key=api_key)


def main():
    # handling empty prompt
    if len(sys.argv) < 2:
        print("You need a prompt 😢")
        sys.exit(1)
    # handling --verbose
    verbose_flag = False
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True
    # declare tools
    try:
    # extracting prompt from sys.arg cli
        prompt = sys.argv[1]
        # prompting gemini
        message = [types.Content(role="user", parts=[types.Part(text=prompt)])]
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=message,
            config=types.GenerateContentConfig(
            tools=[available_functions],  system_instruction=SystemPrompts.AI_CODE_ASSISTANT, temperature=0
            ),
        ) 
        print(response.text)
    except Exception as e:
        return f"Error: unable to generate response >>> {e}"
    if response is None or response.usage_metadata is None:
        print("print is misinformed")
        return
    
    if verbose_flag:
        print(f"User Prompt: {prompt}")
        print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response Tokens:{response.usage_metadata.candidates_token_count}")

    if response.function_calls:
        for function_call in response.function_calls:
         result =  call_function(function_call,verbose_flag)
         print(result)
    function_responses = []
    for function_call in response.function_calls:
        result = call_function(function_call, verbose=verbose_flag)
        if (
            not result.parts
            or not result.parts[0].function_response
            or not result.parts[0].function_response.response
        ):
            raise RuntimeError(f"Empty function response for {function_call.name}")
    if verbose_flag:
            print(f"-> {result.parts[0].function_response.response}")
    function_responses.append(result.parts[0])   

print(main())
