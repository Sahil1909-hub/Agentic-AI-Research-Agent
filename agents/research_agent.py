from langchain_core.messages import (
    SystemMessage, ToolMessage
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

    logger.info("Research Agent Started")

    messages = [
        SystemMessage(
            content="""
            You are an expert research agent.
            Use the web_search tool whenever
            external information is required.
            """
        )
    ] + state["messages"]

    response = research_llm.invoke(messages)

    logger.info(f"Tool Calls: {response.tool_calls}")

    tool_messages = [
    msg.content
    for msg in state["messages"]
    if isinstance(msg, ToolMessage)
]

    web_results = "\n\n".join(tool_messages)

    return {
        "messages": [response],
        "web_results": web_results,
        "research_iterations":
            state.get("research_iterations", 0) + 1
    }