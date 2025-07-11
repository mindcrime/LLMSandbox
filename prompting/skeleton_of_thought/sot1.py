#!/bin/env python3

from openai import OpenAI
import asyncio


async def main():

    print( "Hello, Skeleton of Thought" )
    
    global client
    client = OpenAI(
        base_url = 'http://chplhllncus1.fogbeam.com:9025/v1',
        api_key='ollama', # required, but unused
    )

    # Example usage
    user = "How can I start an MSSP business?"
    
    response = ask_chatgpt(user)

    # print(response)

    lines = response.splitlines()

    skeleton_responses = await process_skeleton_points( user, lines )

    final_answer = assemble_final_answer( skeleton_responses )

    print( final_answer )
    
    print( "done" )

async def process_skeleton_points( user, points ):

    skeleton_responses = []
    tasks = []
    for point in points:
        # print( point )

        task =  asyncio.create_task( expand_skeleton_point( user, point ))
        tasks.append( task )

    for task in tasks:
       skeleton_response = await task
       skeleton_responses.append( skeleton_response )
        
    return skeleton_responses
    
async def expand_skeleton_point( original_user_prompt, skeleton_point ):

    print( "Processing skeleton point: ", skeleton_point )
    system_prompt = """You’re an analyst responsible for only giving answers to specific portions of a complex problem solving process.
    You are being provided the user's original question, and one previously generated 'skeleton point' identifying a portion of the process.
    Your job is to expand on that skeletal point and provide a much more complete and fully fleshed out answer specific to this skeleton point.
    Write only information about the supplied skeleton point, DO NOT provide any additional response about the original question, beyond what
    is directly referenced in the skeleton point. 
    """
    
    user_message = """<original_question>""" + original_user_prompt + """</original_question><skeleton_point>""" + skeleton_point + """</skeleton_point>"""


    response = client.chat.completions.create(
        model="llama3",  # gpt-4 turbo or a model of your preference
        messages=[ { "role": "system", "content": system_prompt },
                  { "role": "user", "content": user_message } ],
        temperature=0.7 )

    
    return response.choices[0].message.content
    
    

def assemble_final_answer( skeleton_responses ):

    # As a first pass, just  aggregate the supplied skeleton answers, don't try to do anything "smart" here just yet.

    answer = "".join( skeleton_responses )

    return answer


    
# Example function to query ChatGPT
def ask_chatgpt(user_message):

    system_prompt = """You’re an analyst responsible for only giving the skeleton (not the full content) for answering the question.
Provide the skeleton in a list of points (numbered 1., 2., 3., etc.) to answer the question. Write a a full, but short sentence, for each 
skeleton point . Each skeleton point should be short with at most 5-10 words. Generally, the skeleton should have 3-10 points. Now,
please provide the skeleton for the following question. List only the bullet points, don't add any preamble or postfix or additional explanation at all."""
    
    response = client.chat.completions.create(
        model="llama3",  # gpt-4 turbo or a model of your preference
        messages=[ { "role": "system", "content": system_prompt },
                  { "role": "user", "content": user_message } ],
        temperature=0.7 )

    
    return response.choices[0].message.content

if __name__ == "__main__":
    # main()
    asyncio.run( main() )
    
