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
        model="gpt-4o-mini", messages=messages, response_format={ "type": "json_object" })

    # print( type( response.choices[0].message.content ) )

    json_object = json.loads(response.choices[0].message.content)

    print( type( json_object ) )
    
    print( json.dumps(json_object, indent=4 ) )
    

if __name__ == "__main__":
    main()
