from langchain_core.messages import (
    SystemMessage
)

from model.llm import llm

from tools.web_search_tool import (
    search_tool
)

from utils.logger import logger


research_llm = llm.bind_tools(
    [search_tool]
)


def research_node(state):

    logger.info(
        "Research Agent Started"
    )

    messages = [
        SystemMessage(
            content=
            """
            You are an expert research agent.

            Use the web_search tool whenever
            external information is required.

            Always gather evidence before answering.
            """
        )
    ] + state["messages"]

    response = research_llm.invoke(
        messages
    )

    return {
        "messages": [response]
    }