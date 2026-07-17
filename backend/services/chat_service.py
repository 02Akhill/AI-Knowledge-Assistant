from backend.database.vector_store import vector_store
from backend.services.gemini_service import create_query_embedding


def retrieve_context(
    question: str,
    top_k: int = 5,
):
    """
    Retrieve the most relevant document chunks
    for a user's question.
    """

    # Generate embedding for the question
    query_embedding = create_query_embedding(question)

    # Search ChromaDB
    results = vector_store.search(
        query_embedding=query_embedding,
        top_k=top_k,
    )

    return results