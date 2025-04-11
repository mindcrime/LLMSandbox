#!/bin/python3

from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader
from llama_index.llms.openai import OpenAI


def main():
    
    print( "Hello, LlamaIndex2" )

    load_dotenv()

    llm = OpenAI(model="gpt-4o-mini")

    documents = SimpleDirectoryReader("data/").load_data()

    index = VectorStoreIndex.from_documents(documents)

    chat_engine = index.as_chat_engine(chat_mode="best", llm=llm, verbose=True)

    response = chat_engine.chat("What are the first programs Paul Graham wrote for Yahoo" )

    print( response )
    
    print( "Done" )
    

    
if __name__ == "__main__":
    
    main()
    
