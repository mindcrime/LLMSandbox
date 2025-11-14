#!../openai-exp/bin/python3

import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

def main():

    load_dotenv(override=True)
    
    client = OpenAI()

    context = [
            {"role": "user", "content": "knock knock."},
            {"role": "assistant", "content": "Who's there?"},
            {"role": "user", "content": "Orange."},
            {"role": "assistant", "content":"Orange who?" },
            {"role": "user", "content":"Orange you glad I didn't say Banana!" }
        ]
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=context
    )
    
    print(response.choices[0].message.content)
    
    
if __name__ == "__main__":
    main()
