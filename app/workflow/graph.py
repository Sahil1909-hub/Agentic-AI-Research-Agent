from typing import TypedDict
from langgraph.graph import StateGraph, END
from app.agents.research_agent import run_research

class AgentState(TypedDict):
    question: str
    answer: str

def research_node(state):
    question = state['question']

    result = run_research(question)

    return {
        "answer": result
    }

graph = StateGraph(AgentState)

graph.add_node("research_agent", research_node)

graph.set_entry_point("research_agent")

graph.add_edge("research_agent", END)

app_graph = graph.compile()

