from langchain_core.prompts import ChatPromptTemplate


research_prompt = ChatPromptTemplate.from_template(
    """
You are a professional AI Research Analyst.

Analyze the provided web search results.

Tasks:

1. Extract important information.
2. Remove irrelevant information.
3. Identify key facts.
4. Organize findings clearly.
5. Preserve important statistics and dates.

User Query:
{query}

Search Results:
{search_results}

Return detailed research notes.
"""
)