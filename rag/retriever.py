from rag.vectorstore import get_vectorstore
from utils.logger import logger

def get_retriever():

    vectorstore = get_vectorstore()

    retriever = vectorstore.as_retriever(
        search_kwargs={"k":4}
    )

    return retriever

logger.info('Retriever created..')