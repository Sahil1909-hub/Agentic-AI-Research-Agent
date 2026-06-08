import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from utils.logger import logger

load_dotenv()

api_key = os.getenv('GROQ_API_KEY')

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=api_key
)
logger.info('Model created..')
