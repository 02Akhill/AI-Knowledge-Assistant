from google import genai

from backend.config import settings


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def create_embeddings(chunks: list[str]):

    embeddings = []

    for chunk in chunks:

        response = client.models.embed_content(
            model="gemini-embedding-2",
            contents=chunk
        )

        embeddings.append(response.embeddings[0])

    return embeddings