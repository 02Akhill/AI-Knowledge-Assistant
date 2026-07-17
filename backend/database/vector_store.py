import chromadb
from chromadb.config import Settings

from backend.models import DocumentChunk


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="chroma_db",
            settings=Settings(
                anonymized_telemetry=False
            )
        )

        self.collection = self.client.get_or_create_collection(
            name="documents",
            metadata={
                "description": "Knowledge Assistant Documents"
            }
        )

    def add_document_chunks(self, chunks: list[DocumentChunk]):

        if not chunks:
            return

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for chunk in chunks:

            ids.append(
                f"{chunk.document_name}_p{chunk.page_number}_c{chunk.chunk_index}"
            )

            documents.append(chunk.text)

            embeddings.append(chunk.embedding)

            metadatas.append(
                {
                    "document_name": chunk.document_name,
                    "page_number": chunk.page_number,
                    "chunk_index": chunk.chunk_index,
                }
            )

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

    def count_documents(self):
        return self.collection.count()

    def get_collection(self):
        return self.collection


vector_store = VectorStore()