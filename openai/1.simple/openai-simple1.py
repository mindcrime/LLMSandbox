#!../openai-exp/bin/python3

from openai import OpenAI
from dotenv import load_dotenv

def main():

    load_dotenv(override=True)

    client = OpenAI()

    response = client.responses.create(
        model="gpt-4.1",
        input="What are you?" )

    print(response.output_text)
    
if __name__ == "__main__":

    main()
    
