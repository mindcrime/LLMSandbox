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


    messages = []
    messages.append( {"role": "user", "content": "What is the weather like in Paris today?"})
    
    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=messages,
        tools=tools )

    print(completion.choices[0].message.tool_calls)

    function_name = completion.choices[0].message.tool_calls[0].function.name
    arguments = completion.choices[0].message.tool_calls[0].function.arguments
    args_dict = json.loads(arguments)
    temperature = globals()[function_name](args_dict['location'])
    
    print( temperature )

    # append the tool call message and a "tool" message with the response from the function
    # call, to the messages list and re-call the LLM

    # print( "Last message: ", completion.choices[0].message )
    
    messages.append(completion.choices[0].message)  # append model's function call message
    
    tool_message = {                               # append result message
        "role": "tool",
        "tool_call_id": completion.choices[0].message.tool_calls[0].id,
        "content": temperature }

    # print( "Tool message: ", tool_message )
    
    messages.append(tool_message)

    completion_2 = client.chat.completions.create(
        model="gpt-4.1",
        messages=messages,
        tools=tools )

    print( completion_2.choices[0].message.content )
    
    
if __name__ == "__main__":
    main()
