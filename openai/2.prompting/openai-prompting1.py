#!../openai-exp/bin/python3

from openai import OpenAI
from dotenv import load_dotenv

def main():

    load_dotenv(override=True)
    client = OpenAI()

    response = client.responses.create(
        model="gpt-4.1",
        input="A few strawberries are in a bowl on the counter, beside a jug of cream. The user puts the turns the bowl upside down, being careful not to disturb the strawberries. They then put the bowl in the microwave and put the cream back in the refrigerator. Where are the strawberries now?" )

    print(response.output_text)
    
if __name__ == "__main__":

    main()
    
