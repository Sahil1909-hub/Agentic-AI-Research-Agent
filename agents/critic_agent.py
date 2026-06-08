from utils.logger import logger
from model.llm import llm
from prompts.critic_prompt import critic_prompt
import json
from langchain_core.messages import HumanMessage


critic_chain = (
    critic_prompt
    | llm
)


def critic_node(state):

    query = state["query"]

    research = (
        state.get("web_results", "")
        or state.get("rag_results", "")
    )

    response = critic_chain.invoke(
        {
            "query": query,
            "research": research
        }
    )

    logger.info(
        f"Research received by critic: {research}"
    )

    ...

    try:

        critique_json = json.loads(
            response.content
        )

        logger.info(
        f"Critic Decision: {critique_json['sufficient']}"
        )

        logger.info(
            f"Follow Ups: {critique_json['follow_up_searches']}"
        )

        return {
            "critique": response.content,
            "sufficient": critique_json["sufficient"],
            "follow_up_searches":
                critique_json["follow_up_searches"]
        }
    
        

    except Exception:

        return {
            "critique": response.content,
            "sufficient": "YES",
            "follow_up_searches": []
        }
    
    