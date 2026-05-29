from langchain_community.vectorstores import FAISS
from app.core.embeddings import embeddings


def create_vectorstore(documents):
    vectorstore = FAISS.from_documents(
        embedding=embeddings,
        documents=documents
    )

    return vectorstore