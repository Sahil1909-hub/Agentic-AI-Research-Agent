from rag.retriever import get_retriever


def vector_search(query: str):

    retriever = get_retriever()

    docs = retriever.invoke(query)

    return docs