#!../openai-exp/bin/python3

import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

def main():

    load_dotenv(override=True)
    
    client = OpenAI()
    messages = []
    
    while True:
        user_input = input(":Enter>   ")
        if user_input == "quit":
            break
        messages.append( {"role": "user", "content": user_input } )
        response = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages)
    
        print(response.choices[0].message.content)
        messages.append(response.choices[0].message )
                         
    print( "Bye..." )
                         
if __name__ == "__main__":
    main()
