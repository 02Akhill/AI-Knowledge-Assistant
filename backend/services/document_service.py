from backend.models import DocumentChunk
from backend.services.file_service import extract_pages
from backend.services.chunk_service import create_chunks


def process_document(pdf_path: str, document_name: str) -> list[DocumentChunk]:
    """
    Extract pages from a PDF and convert them into DocumentChunk objects.
    """

    pages = extract_pages(pdf_path)

    # Debug information
    print(f"Pages extracted: {len(pages)}")

    for page in pages[:5]:
        print(
            f"Page {page.page_number} "
            f"Characters: {len(page.text)}"
        )

    document_chunks: list[DocumentChunk] = []

    chunk_index = 0

    for page in pages:

        chunks = create_chunks(page.text)

        for chunk in chunks:

            document_chunks.append(
                DocumentChunk(
                    document_name=document_name,
                    page_number=page.page_number,
                    chunk_index=chunk_index,
                    text=chunk,
                    embedding=None
                )
            )

            chunk_index += 1

    return document_chunks