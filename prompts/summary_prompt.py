from langchain_core.prompts import ChatPromptTemplate
from utils.logger import logger


summary_prompt = ChatPromptTemplate.from_template(
"""
You are a Senior AI Research Assistant.

User Query:
{query}

Web Research:
{web_results}

Document Research:
{rag_results}

Research Review:
{critique}

Instructions:

1. Answer the user's question directly.
2. Use web and document research.
3. Ignore reviewer comments that are not necessary for answering the query.
4. Do NOT mention missing information unless it prevents answering the question.
5. Do NOT include critique, reviewer notes, limitations, or follow-up searches in the final answer.
6. Produce a professional and complete response.

Return only the final answer.
"""
)