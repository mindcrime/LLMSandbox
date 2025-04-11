#!/bin/python3

from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader
from llama_index.llms.openai import OpenAI


def main():
    
    print( "Hello, LlamaIndex3" )

    load_dotenv()

    llm = OpenAI(model="gpt-4o-mini")

    documents = SimpleDirectoryReader("data/").load_data()

    index = VectorStoreIndex.from_documents(documents)

    chat_engine = index.as_chat_engine(chat_mode="best", llm=llm, verbose=True)

    while True:

        textInput = input( "User: ")

        if textInput == "exit":
            break
        #endif

        response = chat_engine.chat( textInput )
        print( f"Agent: {response}")

    
if __name__ == "__main__":
    
    main()
    
