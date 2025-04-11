'''
Created on Jun 9, 2024

@author: prhodes
'''

import warnings
import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAI
from langchain.schema import (AIMessage, SystemMessage, HumanMessage)
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SimpleSequentialChain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from pinecone import Pinecone as PineCone
from langchain.vectorstores import Pinecone



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
                                    template="Take the concept description of {ml_concept} and explain it to me like Im five, in about 500 words" )
    
    chain_two = LLMChain( llm=chat, prompt=second_prompt )
    
    overall_chain = SimpleSequentialChain( chains=[chain, chain_two], verbose=True )
    
    explanation = overall_chain.run( "autoencoder" )
    
    print( explanation )
    
    text_splitter = RecursiveCharacterTextSplitter( chunk_size = 100, chunk_overlap = 0)
    
    texts = text_splitter.create_documents([explanation])
    
    # print( texts )
    
    # print( "Texts[0]:\n", texts[0].page_content )
    
    embeddings = OpenAIEmbeddings()
    embeddings.tiktoken_model_name = "ada"
    
    query_result = embeddings.embed_query(texts[0].page_content)
    
    print( query_result )
    
    environment=os.getenv( "PINECONE_ENV" )
    print( "Environment: ", environment )
    pc = PineCone(api_key=os.getenv( "PINECONE_API_KEY" ), environment=environment, project_name="Default", host="langchain-exp1-ymkg7lp.svc.aped-4627-b74a.pinecone.io" )
    
    # pinecone.init(api_key, host, environment, project_name, log_level, openapi_config, config)
    
    search = Pinecone.from_documents( texts, embeddings, index_name="langchain-exp1")

    query = "What is magical about an autoencoder?"
    result = search.similarity_search( query )
    
    print( result )
    
    

if __name__ == '__main__':
    main()