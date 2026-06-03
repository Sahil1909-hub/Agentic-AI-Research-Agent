from model.llm import llm
from tools.vector_search_tool import retrieve_documents
from utils.logger import logger


rag_llm = llm.bind_tools(
    [retrieve_documents]
)

def rag_node(state):

    logger.info("RAG agent started")

    response = rag_llm.invoke(
        state['messages']
    )

    logger.info("RAG agent finished")

    return {
        "messages": [response]
    }

