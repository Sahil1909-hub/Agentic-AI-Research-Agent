from typing import TypedDict

class AgentState(TypedDict):

    query: str

    route: str

    web_results: str

    rag_results: str

    critique: str

    summary: str

    final_answer: str

    