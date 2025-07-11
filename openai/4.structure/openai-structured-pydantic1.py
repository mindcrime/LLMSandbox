#!../openai-exp/bin/python3

import os
import sys
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


def main():
    
    print("Hello from openai!")

    load_dotenv(override=True)
    
    client = OpenAI()

    completion = client.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "Extract the event information."},
            {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."} ],

        response_format=CalendarEvent)

    event = completion.choices[0].message.parsed

    print( type( event ) )
    print( f"Event: {event.name}, Date: {event.date}, Participants: {event.participants}" )
    

if __name__ == "__main__":
    main()
