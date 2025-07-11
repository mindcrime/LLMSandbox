#!../openai-exp/bin/python3

from openai import OpenAI
from dotenv import load_dotenv

def main():

    load_dotenv(override=True)
    client = OpenAI()

    response = client.responses.create(
        model="gpt-4.1",
        input=" How many R's are in Strawberry?" )

    
    # Exercise: how much "stuff" (especially gibberish) can we add to the context before the LLM starts to get confused??
    
    print(response.output_text)
    
if __name__ == "__main__":

    main()
    
