from langchain.tools import tool
from rag.vectorstore import load_vectorstore

# Load vectorstore once at startup
vectorstore = load_vectorstore()
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

@tool
def symptom_rag_tool(query: str) -> str:
    """
    Searches the medical knowledge base to answer health-related questions.
    Use this when the user describes symptoms or asks about a medical condition.
    Input: a symptom or medical question in natural language.
    Output: relevant medical information with recommended specialty.
    """
    docs = retriever.invoke(query)

    if not docs:
        return "Aucune information trouvée dans la base médicale."

    results = []
    for i, doc in enumerate(docs):
        results.append(f"Source {i+1}:\n{doc.page_content}")

    return "\n\n".join(results)