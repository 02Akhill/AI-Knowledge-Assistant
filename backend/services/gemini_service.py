from google import genai

from backend.config import settings
from backend.models import DocumentChunk


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


# ==========================================
# Create Document Embeddings
# ==========================================

def create_embeddings(
    document_chunks: list[DocumentChunk],
) -> list[DocumentChunk]:
    """
    Generate embeddings for all document chunks.
    """

    for chunk in document_chunks:

        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=chunk.text
        )

        chunk.embedding = response.embeddings[0].values

    return document_chunks


# ==========================================
# Create Query Embedding
# ==========================================

def create_query_embedding(
    question: str,
) -> list[float]:
    """
    Generate an embedding for the user's question.
    """

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=question
    )

    return response.embeddings[0].values