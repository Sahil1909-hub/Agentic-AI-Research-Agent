from langchain_tavily import TavilySearch
from langchain.tools import tool
from utils.logger import logger
from dotenv import load_dotenv

load_dotenv()

tavily_search = TavilySearch(
    max_results=5
)

@tool
def search_tool(query: str):
    """
    Search the web for recent information.
    Use this tool whenever internet research is required.
    """

    logger.info(
        f"Web Search Tool Called: {query}"
    )

    try:

        search_result = tavily_search.invoke(query)

        return str(search_result)

    except Exception as e:

        logger.error(
            f"Web Search Error: {e}"
        )

        return f"Error: {str(e)}"