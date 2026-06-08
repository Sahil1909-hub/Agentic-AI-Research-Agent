from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages


class AgentState(TypedDict):

    messages: Annotated[list, add_messages]

    query: str
    route: str

    document_uploaded: bool

    web_results: str
    rag_results: str

    critique: str
    summary: str
    final_answer: str

    research_iterations: int
    sources: list

    follow_up_searches: list[str]
    sufficient: str