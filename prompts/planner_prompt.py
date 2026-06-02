from langchain_core.prompts import ChatPromptTemplate


planner_prompt = ChatPromptTemplate.from_template(
    """
You are an expert routing agent.

Your job is to decide how a user query should be processed.

Available routes:

WEB
- Use when the query requires internet research.
- Use when latest information is needed.

RAG
- Use when the answer can be found only in uploaded documents.

BOTH
- Use when both internet information and uploaded documents are required.

Return ONLY one word:

WEB
RAG
BOTH

User Query:
{query}
"""
)