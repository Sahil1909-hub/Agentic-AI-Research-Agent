from model.llm import llm
from tools.vector_search_tool import retrieve_documents
from utils.logger import logger


def rag_node(state):

    logger.info("RAG agent started")

    query = state["messages"][-1].content

    context = retrieve_documents.invoke(query)

    response = llm.invoke(
        f"""
        Answer the question using the context below.

        Context:
        {context}

        Question:
        {query}
        """
    )

    logger.info("RAG agent finished")

    return {
        "messages": [response],
        "query": query,
        "rag_results": context
    }