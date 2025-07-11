#!../openai-exp/bin/python3

import os
import sys
from openai import OpenAI
from dotenv import load_dotenv


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

    
    
if __name__ == "__main__":
    main()
