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

        docs = retriever.invoke(query)

        print("\n===== RETRIEVED DOCS =====\n")

        for i, doc in enumerate(docs):
            print(f"\n--- DOC {i+1} ---")
            print(doc.page_content[:500])

        print("\n==========================\n")

        if not docs:
            return "No relevant documents found."
        
        context = "\n\n".join(
            [
                doc.page_content for doc in docs
            ]
        )

        print("\n========== RETRIEVED ==========\n")
        print(context[:1000])
        print("\n===============================\n")

        return context
    
    except Exception as e:

        logger.error(
            f"Retriever Error: {e}"
        )

        return f"Error: {str(e)}"
