#!../openai-exp/bin/python3

import os
import sys
from openai import OpenAI
from dotenv import load_dotenv
import json

def main():
    
    print("Hello from openai!")

    load_dotenv(override=True)
    
    client = OpenAI()

    messages = []

    messages.append( {"role":"user", "content":"Give me a list of 10 redneck jokes. Please return them in JSON format."} )
    
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages, response_format={ "type": "json_schema", "json_schema": {
             "schema": {
                 "type": "object",
                 "properties": {
                   "setup": {"type": "string"},
                   "humor_score": {"type": "number", "minimum": 0, "maximum": 1},
                   "punch_line": {"type": "string"}
              }
             },
            "name":"redneck_joke"
           }
        })

    print( type( response.choices[0].message.content ) )
    
    print( response.choices[0].message.content )
        

if __name__ == "__main__":
    main()
