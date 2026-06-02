from langchain_huggingface import HuggingFaceEmbeddings
from utils.logger import logger

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

logger.info('Embeddings created..')

