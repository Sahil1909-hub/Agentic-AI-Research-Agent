from langchain_tavily import TavilySearch
from app.config.settings import TAVILY_API_KEY

search_tool = TavilySearch(max_results=5)

