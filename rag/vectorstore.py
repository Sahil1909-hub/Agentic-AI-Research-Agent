from langchain_chroma import Chroma
from rag.embeddings import embeddings
from utils.logger import logger


def get_vectorstore():

    chroma_path = "chroma_db"

    vectorstore = Chroma(
        embedding_function=embeddings,
        persist_directory=chroma_path
    )

    return vectorstore


logger.info('Vectorstore created..')