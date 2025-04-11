#!/bin/python3

from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader
from llama_index.llms.openai import OpenAI

def main():
    
    print( "Hello, LlamaIndex World!\n")

    load_dotenv()

    OpenAI(model="gpt-4o-mini")

    documents = SimpleDirectoryReader("data/").load_data()

    index = VectorStoreIndex.from_documents(documents)

    query_engine = index.as_query_engine()

    query = input( "What would you like to know?\n\n" )
    
    response = query_engine.query( query )

    print( response )
    
    print( "Done" )
    
if __name__ == "__main__":
    main()
    
