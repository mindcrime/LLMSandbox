#!../openai-exp/bin/python3

import os
import sys
from openai import OpenAI
from dotenv import load_dotenv
import json

def get_weather(location:str) -> str:

    print( location )
    
    if location == "Paris, France":
        return "90"
    else:
        return "76"

def main():
    
    print("Hello from openai!")

    load_dotenv(override=True)
    
    client = OpenAI()

    tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current temperature for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City and country e.g. Bogotá, Colombia"
                }
            },
            "required": [
                "location"
            ],
            "additionalProperties": False
        },
        "strict": True
    }
}]
    
    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": "What is the weather like in Paris today?"}],
        tools=tools )

    print(completion.choices[0].message.tool_calls)

    function_name = completion.choices[0].message.tool_calls[0].function.name
    arguments = completion.choices[0].message.tool_calls[0].function.arguments
    args_dict = json.loads(arguments)


    
    temperature = globals()[function_name](args_dict['location'])
    
    print( temperature )

    
if __name__ == "__main__":
    main()
