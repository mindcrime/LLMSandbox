'''
Created on Jun 9, 2024

@author: prhodes
'''

from dotenv import load_dotenv, find_dotenv

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from langchain.schema import (AIMessage, SystemMessage, HumanMessage)


def main():
    
    print("Hello Langchain World\n")
    
    load_dotenv(find_dotenv())    
    
    chat = ChatOpenAI( model_name = "gpt-4o", temperature=0.5 )
    messages = [ SystemMessage(content="You are a useless assistant!"), HumanMessage(content="Explain how LLM's work, in one sentence.") ]
    
    response = chat(messages)
    
    print(response.content)
    
    messages.append(AIMessage(content=response.content))
    
    messages.append(HumanMessage(content="How do you know that?"))
    
    response = chat(messages)
    
    print(response.content)
    

if __name__ == '__main__':
    main()