#!/bin/python3

import os
from dotenv import load_dotenv
import nest_asyncio
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex


def main():

    print( "Hello, LlamaParse7!" )

    load_dotenv()

    llama_parse_api_key = os.getenv( "LLAMA_PARSE_API_KEY" )

    # print( "llama_parse_api_key: ", llama_parse_api_key )
    
    parser = LlamaParse( api_key = llama_parse_api_key,
                         result_type="markdown",
                         verbose=True )


    file_extractor = {".pdf":parser}

    documents = SimpleDirectoryReader("./pdf/", file_extractor=file_extractor ).load_data()

    index = VectorStoreIndex.from_documents( documents )

    query_engine = index.as_query_engine()
    
    response = query_engine.query( "What can LlamaIndex be used for?" )

    print( response )
    
    print( "Done" )
    

if __name__ == "__main__":

    main()
    
