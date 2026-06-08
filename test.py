# from langchain_core.messages import HumanMessage
# from graph.graph import graph


# result = graph.invoke(
#     {
#         "messages": [
#             HumanMessage(
#                 content="Summarize the uploaded document"
#             )
#         ]
#     },
#     config={
#         "configurable": {
#             "thread_id": "1"
#         }
#     }
# )

# print("\n")
# print(result["final_answer"])
# print("\n")

from rag.vectorstore import get_vectorstore

vectorstore = get_vectorstore()

results = vectorstore.similarity_search(
    "What is HTML?",
    k=3
)

print(results)

print(
    vectorstore._collection.count()
)