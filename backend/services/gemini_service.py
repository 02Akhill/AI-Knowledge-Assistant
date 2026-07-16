from google import genai

from backend.config import settings
from backend.models import DocumentChunk


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def create_embeddings(
    document_chunks: list[DocumentChunk],
) -> list[DocumentChunk]:

    for chunk in document_chunks:

        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=chunk.text
        )

        chunk.embedding = response.embeddings[0].values

    return document_chunks