from utils.logger import logger

from model.llm import llm

from prompts.summary_prompt import (
    summary_prompt
)


summary_chain = (
    summary_prompt
    | llm
)


def summarizer_node(state):

    logger.info(
        "Summarizer Agent Started"
    )

    query = state["messages"][-1].content

    response = summary_chain.invoke(
        {
            "query": query,
            "web_results": state.get(
                "web_results",
                ""
            ),
            "rag_results": state.get(
                "rag_results",
                ""
            ),
            "critique": state.get(
                "critique",
                ""
            )
        }
    )

    logger.info(
        "Summary Generated"
    )

    return {
        "summary": response.content,
        "final_answer": response.content
    }