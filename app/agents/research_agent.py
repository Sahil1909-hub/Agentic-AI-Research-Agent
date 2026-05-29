from app.tools.web_search import search_tool
from app.core.llm import llm


def run_research(query):

    # Step 1: Web Search
    search_results = search_tool.invoke(query)

    formatted_results = ""

    for idx, result in enumerate(search_results, start=1):

        if isinstance(result, dict):

            title = result.get("title", "No Title")
            content = result.get("content", "No Content")
            url = result.get("url", "")

            formatted_results += f"""
            Source {idx}

            Title:
            {title}

            Content:
            {content}

            URL:
            {url}

            ------------------------
            """

    # Step 2: Research Prompt
    final_prompt = f"""
    You are a professional AI Research Assistant.

    User Query:
    {query}

    Web Research Results:
    {formatted_results}

    Your task:
    - Analyze all sources carefully
    - Give a detailed research-based answer
    - Mention key insights
    - Keep answer structured
    - Mention important findings
    - Do not hallucinate
    - Use professional formatting
    """

    response = llm.invoke(final_prompt)

    return response.content