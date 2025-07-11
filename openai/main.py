#!../openai-exp/bin/python3

import os
import sys
from openai import OpenAI
from dotenv import load_dotenv


def main():
    
    print("Hello from openai!")

    load_dotenv(override=True)
    
    client = OpenAI()

    messages = []

    messages.append( {"role":"user", "content":""} )
    
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages)
    
    print(response.choices[0].message.content)

    

if __name__ == "__main__":
    main()
