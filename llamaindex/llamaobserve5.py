#!/bin/python3


from dotenv import load_dotenv
import os
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader,StorageContext,load_index_from_storage,get_response_synthesizer,set_global_handler


def main():
    print( "Hello, LlamaObserve5" )

    load_dotenv()

    PHOENIX_API_KEY = os.getenv("PHOENIX_API_KEY")

    os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"api_key={PHOENIX_API_KEY}"


    set_global_handler( "arize_phoenix", endpoint="https://llamatrace.com/v1/traces" ) 

    documents = SimpleDirectoryReader("data/").load_data()

    if os.path.exists("storage"):
        print( "Loading index from storage...")
        storage_context = StorageContext.from_defaults(persist_dir="storage")
        index = load_index_from_storage(storage_context)
    else:
        print( "Creating the new index" )
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist( persist_dir="storage" )

        
    query_engine = index.as_query_engine()

    response = query_engine.query( "What does Paul Graham think about Lisp for startup founders?" )

    print( response )
        
    print( "Done" )

    
if __name__ == "__main__":
    main()
    
