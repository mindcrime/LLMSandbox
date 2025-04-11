#!/bin/python3

import os
from dotenv import load_dotenv
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
 


def main():

    print( "Hello, LlamaIndex6" )


    load_dotenv()

    llm = OpenAI(model="gpt-4o")

    add_tool = FunctionTool.from_defaults(fn=add)
    multiply_tool = FunctionTool.from_defaults(fn=multiply)
    subtract_tool = FunctionTool.from_defaults(fn=subtract)
    divide_tool = FunctionTool.from_defaults(fn=divide)
    
    agent = ReActAgent.from_tools( [add_tool,multiply_tool,subtract_tool,divide_tool],llm=llm,verbose=True )


    response = agent.chat( "What is the sum of nineteen and twenty-eight?" )

    print( "Response: ", response )
    
    
    print( "Done" )
    

# Functions
def add( a: float, b: float ) -> float:
    """Add two numbers and return the sum. Return a+b"""

    return a+b

def multiply( a: float, b: float ) -> float:
    """Multiply two numbers and return the product. Return a*b"""

    return a*b

def subtract( a: float, b: float ) -> float:
    """Subtract two numbers and return the difference. Return a-b"""

    return a-b

def divide( a: float, b: float ) -> float:
    """Divide two numbers and return the quotient. Return a/b"""

    return a/b

    
if __name__ == "__main__":
    
    main()
