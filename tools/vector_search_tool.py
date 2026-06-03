from rag.retriever import get_retriever
from utils.logger import logger
from langchain.tools import tool

@tool
def retrieve_documents(query: str):
    """
    Search the vector database and retrieve
    relevant document chunks.
    """

    logger.info(
        f"Vector Search Called: {query}"
    )

    try:
        retriever = get_retriever()

        docs = retriever.invoke(query)

        if not docs:
            return "No relevant documents found."
        
        context = "\n\n".join(
            [
                doc.page_content for doc in docs
            ]
        )

        return context
    
    except Exception as e:

        logger.error(
            f"Retriever Error: {e}"
        )

        return f"Error: {str(e)}"

    return docs