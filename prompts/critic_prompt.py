from langchain_core.prompts import ChatPromptTemplate


critic_prompt = ChatPromptTemplate.from_template(
    """
You are a Senior AI Critic Agent.

Review the information collected by other agents.

Tasks:

1. Identify missing information.
2. Identify weak arguments.
3. Detect contradictions.
4. Detect unsupported claims.
5. Suggest improvements.

User Query:
{query}

Web Research:
{web_results}

Document Research:
{rag_results}

Provide a detailed critique.
"""
)