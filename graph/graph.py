from langgraph.graph import StateGraph, START, END
from graph.tool_node import web_tool_node, rag_tool_node
from graph.routing import route_query
from langgraph.checkpoint.memory import MemorySaver
from agents.critic_agent import critic_node
from agents.planner_agent import planner_node
from agents.rag_agent import rag_node
from agents.research_agent import research_node
from agents.summarizer_agent import summarizer_node
from graph.state import AgentState
from langgraph.prebuilt import tools_condition


memory = MemorySaver()


builder = StateGraph(AgentState)

builder.add_node("planner", planner_node)
builder.add_node("research", research_node)
builder.add_node("web_tools", web_tool_node)
builder.add_node("rag", rag_node)
builder.add_node("critic", critic_node)
builder.add_node("summarizer", summarizer_node)


builder.add_edge(START,"planner")
builder.add_conditional_edges(
    "planner", route_query,
    {
        "research":"research",
        "rag":"rag"
    })
                              

builder.add_conditional_edges(
    "research",
    tools_condition,
    {
        "tools": "web_tools",
        "__end__": "critic"
    }
)

builder.add_edge("web_tools", "research")
builder.add_edge("rag","critic")
builder.add_edge("critic", "summarizer")
builder.add_edge("summarizer", END)


graph = builder.compile(
    checkpointer=memory
)





