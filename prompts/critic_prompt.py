from langchain_core.prompts import ChatPromptTemplate
from utils.logger import logger


critic_prompt = ChatPromptTemplate.from_template("""
You are a research critic.

Analyze the research answer carefully.

Determine whether the information is sufficient to answer the user query.

Return ONLY valid JSON.                                         
                                                 

Schema:

{{
  "sufficient": "YES or NO",
  "missing_information": [],
  "follow_up_searches": []
}}

User Query:
{query}

Research Findings:
{research}
""")

logger.info("Critic prompt created")