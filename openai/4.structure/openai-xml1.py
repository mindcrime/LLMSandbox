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

    messages.append( {"role":"user", "content":"Give me a list of 10 redneck jokes. Please return them in XML format. For the xml use something like the following for the schema: <RedneckJokes><joke><joke_id></joke_id><setupLine></setupLine><punchLine></punchLine></joke></RedneckJokes>"} )
    
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages)
    
    print(response.choices[0].message.content)

    

if __name__ == "__main__":
    main()
