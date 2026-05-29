from app.core.vectorstore import create_vectorstore

def build_retriever(documents):
    vectorstore = create_vectorstore(documents=documents)

    retriever = vectorstore.as_retriever(
        search_type = "similarity",
        search_kwargs = {"k":4}
    )

    return retriever