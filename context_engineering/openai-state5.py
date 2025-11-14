#!../openai-exp/bin/python3

import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

def main():

    load_dotenv(override=True)
    
    client = OpenAI()

    context= []
    
    while True:
        user_input = input(":Enter>   ")
        if user_input == "quit":
            break
        elif user_input == "/clear":
            user_input = None
            context = []

        if user_input == None:
            continue
        
        context.append( {"role": "user", "content": user_input } )
        response = client.chat.completions.create(
            model="gpt-4o-mini", messages=context)
    
        print(response.choices[0].message.content)
        context.append(response.choices[0].message )
                         
    print( "Bye..." )
                         
if __name__ == "__main__":
    main()
