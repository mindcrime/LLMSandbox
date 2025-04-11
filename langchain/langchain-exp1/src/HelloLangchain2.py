'''
Created on Jun 9, 2024

@author: prhodes
'''

from dotenv import load_dotenv, find_dotenv

# from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
# from langchain.schema import (AIMessage, SystemMessage, HumanMessage)


def main():
    
    print("Hello Langchain World\n")
    
    load_dotenv(find_dotenv())    
    
    llm = OpenAI( temperature=0.5)
    
    # previously llm( "How to say 'The glass is good' in German?" ) - but this form is deprecated. Use invoke() now
    print( llm.invoke("How to say 'The glass is good' in German?"), "\n" )
    
    print( "Done" )
    

if __name__ == '__main__':
    main()