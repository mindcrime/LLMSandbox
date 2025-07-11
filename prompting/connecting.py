#!/bin/env python3

from openai import OpenAI

def main():
    
    global client
    client = OpenAI(
        # base_url = 'http://morpheus:8080/v1',
        base_url = 'http://chplhllncus1.fogbeam.com:9025/v1',
        api_key='ollama', # required, but unused
    )

    # Example usage
    user = "What is the capital of France?"
    response = ask_chatgpt(user)
    print(response)
    
# Example function to query ChatGPT
def ask_chatgpt(user_message):
    response = client.chat.completions.create(
        model="llama3",  # gpt-4 turbo or a model of your preference
        messages=[{"role": "system", "content": "You are a neurotic, and mostly satanic, assistant."},
                  {"role": "user", "content": user_message}],
        temperature=0.7,
        )       
    return response.choices[0].message.content

if __name__ == "__main__":
    main()
    
