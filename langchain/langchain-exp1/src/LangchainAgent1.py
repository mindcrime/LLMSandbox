'''
Created on Aug 9, 2024

@author: prhodes
'''

from dotenv import load_dotenv, find_dotenv
import os

def main():
    
    print( "Hello, Langchain Agents!" )
    
    load_dotenv(find_dotenv())
    
    # print( os.getenv( "SERP_API_KEY" ) )
    
    
    
    print( "Done" )
    

if __name__ == '__main__':
    main()
    
    