from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph.message import add_messages


class AgentState(TypedDict):

    messages: Annotated[
        list,
        add_messages
    ]

    route: str

    web_results: str

    rag_results: str

    critique: str

    summary: str

    final_answer: str