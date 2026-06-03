from langchain_community.document_loaders import PyPDFLoader
from utils.logger import logger

def load_pdf(path: str):

    loader = PyPDFLoader(path)

    documents = loader.load()

    return documents


logger.info('Pdf loader tool created..')