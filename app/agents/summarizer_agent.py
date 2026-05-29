from app.core.llm import llm
from langchain_classic.prompts import ChatPromptTemplate
from app.prompts.summary_prompt import summary_prompt

prompt = ChatPromptTemplate.from_template(summary_prompt)

summarizer_chain = prompt | llm

def summarize_research(content):
    response = summarizer_chain.invoke({
        "input": content
    })

    return response.content