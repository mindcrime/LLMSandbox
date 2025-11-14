#!../openai-exp/bin/python3

import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

def main():

    load_dotenv(override=True)
    
    client = OpenAI()

    context = []

    print( "knock, knock" )
    context.append( {"role": "user", "content": "knock knock."} )
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=context
    )

    print(response.choices[0].message.content)
    
    # add previous response to the context
    context.append( response.choices[0].message )

    # and add our next prompt to the context
    print( "Orange" )
    context.append( {"role": "user", "content": "Orange."} )

    
    # Now call the LLM again with the previous response and our new part
    # tacked onto the context

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=context
    )

    print(response.choices[0].message.content)


    # add previous response to the context
    context.append( response.choices[0].message )

    # and add our next prompt to the context
    print( "Orange you glad I didn't say Banana!" )
    context.append( {"role": "user", "content": "Orange you glad I didn't say Banana!"} )

    
    # Now call the LLM again with the previous response and our new part
    # tacked onto the context

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=context
    )

    print(response.choices[0].message.content)
    

    
if __name__ == "__main__":
    main()
