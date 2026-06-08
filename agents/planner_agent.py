from utils.logger import logger
from model.llm import llm
from prompts.planner_prompt import planner_prompt


planner_chain = planner_prompt | llm


def planner_node(state):

    logger.info(
        "Planner agent started"
    )

    query = state["messages"][-1].content

    response = planner_chain.invoke(
        {
            "query": query
        }
    )

    route = response.content.strip().upper()

    if state.get("document_uploaded", False):
        route = "RAG"

    logger.info(
        f"Route Selected: {route}"
    )

    return {
        "route": route,
        "query": query,
        "research_iterations": 0,
        "sources": [],
        "follow_up_searches": [],
        "sufficient": "NO"
    }