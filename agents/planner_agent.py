from utils.logger import logger
from prompts.planner_prompt import planner_prompt
from model.llm import llm

planner_chain = planner_prompt | llm

def planner_node(state):

    logger.info("Planner agent started")

    response = planner_prompt.invoke({
        "query": state["query"]
    })

    route = response.content.strip()

    logger.info(
        f"Route Selected: {route}"
    )

    return {
        "route": route
    }