import os
from openai import OpenAI
from langchain_openai import ChatOpenAI
from typing import Literal
from tavily import TavilyClient

# HERE
from deepagents import create_deep_agent
from dotenv import load_dotenv
from langchain_core.runnables import RunnableConfig


# Search tool to use to do research
def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
        include_raw_content: bool = False ):    
    """Run a web search"""

    
    tavily_client = TavilyClient(api_key=tavily_api_key)

    return tavily_client.search( query, max_results=max_results,
                                 include_raw_content=include_raw_content, topic=topic )

def main():

    load_dotenv(override=True)
    
    print("Hello from simple-agent!")

    global tavily_api_key
    tavily_api_key = os.getenv( "TAVILY_API_KEY" )

    # print( "TAVILY_API_KEY: ", tavily_api_key )
    
    llm = ChatOpenAI()
    
    # Prompt prefix to steer the agent to be an expert researcher
    research_instructions = """You are an expert researcher. Your job is to conduct thorough research, 
    and then write a polished report.

    You have access to a few tools.

    ## `internet_search`

    Use this to run an internet search for a given query. You can specify the number of results, the 
    topic, and whether raw content should be included.
    """

    # Create the agent
    agent = create_deep_agent( [internet_search],  research_instructions, model=llm )

    config = RunnableConfig(recursion_limit=100)

    # output = runnable.invoke(input_data, config=config)
    
    # Invoke the agent
    result = agent.invoke({"messages": [{"role": "user", "content": "what is langgraph?"}]}, config=config)

    # print( type( result['messages'][-1] ) )
    # print(  dir( result['messages'][-1] ) )
    
    print( result['messages'][-1].content )
    
    
if __name__ == "__main__":
    main()
