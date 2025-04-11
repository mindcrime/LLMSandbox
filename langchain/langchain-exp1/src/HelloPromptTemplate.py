'''
Created on Jun 9, 2024

@author: prhodes
'''

import warnings
from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAI
from langchain.schema import (AIMessage, SystemMessage, HumanMessage)
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SimpleSequentialChain


def main():
    warnings.filterwarnings("ignore")    
    print("Hello Langchain World\n")
    load_dotenv(find_dotenv())
    
    chat = ChatOpenAI( model_name = "gpt-4o", temperature=0.5 )
    messages = [ SystemMessage(content="You are a useless assistant!"), HumanMessage(content="Explain how LLM's work, in one sentence.") ]
    
    template = """
    You are an expert data scientist, with an expertise in developing deep learning models.
    Explain the concept of {concept} in a couple of lines.
    """
    
    prompt = PromptTemplate(input_variables=["concept"], template=template)
    
    # print( prompt.format(concept="autoencoder") )
    # messages.append( HumanMessage(content=prompt.format(concept="autoencoder")))

    # response = chat(messages)
    # print(response.content)

    chain = LLMChain( llm=chat, prompt=prompt )
    
    # print( chain.run("autoencoder"))

    second_prompt = PromptTemplate( input_variables=['ml_concept'],
                                    template="Take the concept description of {ml_concept} and explain it to me like Im five." )
    
    chain_two = LLMChain( llm=chat, prompt=second_prompt )
    
    overall_chain = SimpleSequentialChain( chains=[chain, chain_two], verbose=True )
    
    explanation = overall_chain.run( "autoencoder" )
    
    print( explanation )
    

if __name__ == '__main__':
    main()