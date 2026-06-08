from langgraph.prebuilt import ToolNode
from tools.vector_search_tool import retrieve_documents
from tools.web_search_tool import search_tool

web_tool_node = ToolNode(
    [search_tool]
)

rag_tool_node = ToolNode(
    [retrieve_documents]
)