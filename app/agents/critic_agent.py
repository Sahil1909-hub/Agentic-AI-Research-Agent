from langchain_core.prompts import ChatPromptTemplate
from app.core.llm import llm
from app.prompts.critique_prompt import critique_prompt


prompt = ChatPromptTemplate.from_template(critique_prompt)

critic_chain = prompt | llm


def critique_response(content):

    response = critic_chain.invoke({
        "input": content
    })

    return response.content