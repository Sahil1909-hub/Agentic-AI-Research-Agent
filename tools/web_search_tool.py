from langchain_tavily import TavilySearch
import os
from dotenv import load_dotenv
from utils.logger import logger
from langchain.tools import tool

load_dotenv()

search_tool = TavilySearch(
        max_results=5
    )


@tool
def search_tool(query: str):
    """ Search the web for recent information.
    Use this tool whenever internet research is required."""

    logger.info(
        f"Web Search Tool Called: {query}"
    )

    try:

        search_result = search_tool.invoke(query)
        
        return str(search_result)
    
    except Exception as e: 

        logger.error(
            f"Web Search Error: {e}"
        )

        return f"Error: {str(e)}"



logger.info('Web search tool created..')