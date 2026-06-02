from langchain_tavily import TavilySearch
import os
from dotenv import load_dotenv
from utils.logger import logger

load_dotenv()

search_tool = TavilySearch(
    max_results=5
)   


logger.info('Web search tool created..')