from langchain_classic.chains import RetrievalQA

from app.core.llm import llm

def build_rag_chain(retriever):
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True
    )

    return qa_chain