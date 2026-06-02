from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag.vectorstore import get_vectorstore
from rag.embeddings import embeddings
from rag.retriever import get_retriever
from tools.pdf_loader_tool import load_pdf
from utils.logger import logger

def ingest_pdf(pdf_path: str):

    logger.info(f"Loading path: {pdf_path}")

    documents = load_pdf(pdf_path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    logger.info(
        f"Created {len(chunks)} chunks"
    )

    vectorstore = get_vectorstore()

    vectorstore.add_documents(
        chunks
    )

    logger.info(
        "Documents stored successfully"
    )

    return len(chunks)



    