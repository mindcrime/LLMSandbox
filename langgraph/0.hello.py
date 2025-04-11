#!.venv/bin/python3

from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    graph_state: str

def node_1(state):
    print("---Node 1---")
    return {"graph_state": state['graph_state'] +" I am I!"}

def main():
    print( "Hello, Example 0!\n")

    builder = StateGraph(State)
    builder.add_node("node_1", node_1)

    # Logic
    builder.add_edge(START, "node_1")
    builder.add_edge("node_1", END)


    graph = builder.compile()

    response = graph.invoke({"graph_state" : "Hi, this is Phil."})
    
    print( response.get('graph_state') )
    
    print( "Done" )
        
if __name__ == "__main__":
    main()


