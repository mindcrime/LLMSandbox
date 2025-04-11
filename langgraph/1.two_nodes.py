#!.venv/bin/python3

from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    graph_state: str

def node_1(state):
    print("---Node 1---")
    return {"graph_state": state['graph_state'] +" I am"}

def node_2(state):
    print("---Node 2---")
    return {"graph_state": state['graph_state'] +" happy!"}

    
def main():
    print( "Hello, Example 1!\n")

    builder = StateGraph(State)
    builder.add_node("node_1", node_1)
    builder.add_node("node_2", node_2)

    # Logic
    builder.add_edge(START, "node_1")
    builder.add_edge( "node_1", "node_2" )
    builder.add_edge("node_2", END)


    graph = builder.compile()

    response = graph.invoke({"graph_state" : "Hi, this is Phil."})
    
    print( response.get('graph_state') )

    print( "Done" )
    
    
if __name__ == "__main__":

    main()
