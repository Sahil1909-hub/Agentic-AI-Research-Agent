from langchain_core.prompts import ChatPromptTemplate
from utils.logger import logger


summary_prompt = ChatPromptTemplate.from_template(
    """
You are an expert AI Research Assistant.

Create a final response using:

1. Web research findings
2. Document findings
3. Critic feedback

Requirements:

- Accurate
- Concise but informative
- Well structured
- Easy to read
- Use headings where appropriate
- Include key facts
- Mention important limitations

User Query:
{query}

Web Research:
{web_results}

Document Research:
{rag_results}

Critic Feedback:
{critique}

Generate the final answer.
"""
)

logger.info('Summary prompt ready..')