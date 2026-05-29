from app.chains.rag_chain import build_rag_chain
from app.tools.retriever import build_retriever

def run_retriever(documents, query):

    retriever = build_retriever(documents)

    rag_chain = build_rag_chain(retriever)

    response = rag_chain.invoke(query)

    return response