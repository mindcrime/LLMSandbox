#!/bin/python3

from dotenv import load_dotenv
import os

import chromadb

from llama_index.core import VectorStoreIndex,SimpleDirectoryReader,StorageContext,load_index_from_storage,get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.openai import OpenAI


def main():
    
    print( "Hello, LlamaIndex4" )

    load_dotenv()

    # 1. Load data

    dir_path = "./chromadb/"
    if not (os.path.exists(dir_path) and os.path.isdir(dir_path)):
        print(f"Directory '{dir_path}' does not exist.")

        documents = SimpleDirectoryReader( "./data/" ).load_data()
    
        # 2. Create index

        db = chromadb.PersistentClient(path="./chromadb/")
    
        chroma_collection = db.get_or_create_collection( "quickstart" )

        vector_store = ChromaVectorStore( chroma_collection=chroma_collection)

        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        index = VectorStoreIndex.from_documents( documents, storage_context=storage_context )

        storage_context.persist(persist_dir=dir_path)
        
    else:
        print(f"Directory '{dir_path}' exists.")
        
        db = chromadb.PersistentClient(path=dir_path)
    
        chroma_collection = db.get_or_create_collection( "quickstart" )

        vector_store = ChromaVectorStore( chroma_collection=chroma_collection)

        # rebuild storage context
        storage_context = StorageContext.from_defaults(persist_dir=dir_path)
        
        # load index
        # index = load_index_from_storage(storage_context)
        index = VectorStoreIndex.from_vector_store(vector_store, storage_context=storage_context)
        
    # 4. Create query engine

    retriever = VectorIndexRetriever( index=index, similarity_top_k=10 )

    response_synthesizer = get_response_synthesizer()

    query_engine = RetrieverQueryEngine( retriever=retriever, response_synthesizer=response_synthesizer, node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.5)] )
    

    response = query_engine.query( "What is the meaning of LISP?" )

    print( response )
    
    print( "Done" )
    
if __name__ == "__main__":
    
    main()
    
