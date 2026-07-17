from fastapi import FastAPI, UploadFile, File, HTTPException

from backend.models import (
    UploadResponse,
    ChatRequest,
    ChatResponse,
)

from backend.services.file_service import save_pdf
from backend.services.document_service import process_document
from backend.services.gemini_service import create_embeddings

from backend.database.vector_store import vector_store


app = FastAPI(
    title="AI Knowledge Assistant",
    version="0.7"
)


# ==========================================
# Home Endpoint
# ==========================================

@app.get("/")
def home():
    return {
        "message": "AI Knowledge Assistant is running."
    }


# ==========================================
# Upload PDFs
# ==========================================

@app.post("/upload", response_model=UploadResponse)
async def upload_pdfs(files: list[UploadFile] = File(...)):

    uploaded_files = []

    try:

        for file in files:

            # ---------------------------------
            # Save PDF
            # ---------------------------------
            pdf_path = await save_pdf(file)

            # ---------------------------------
            # Process Document
            # ---------------------------------
            document_chunks = process_document(
                pdf_path=pdf_path,
                document_name=file.filename
            )

            # ---------------------------------
            # Generate Embeddings
            # ---------------------------------
            document_chunks = create_embeddings(document_chunks)

            # ---------------------------------
            # Store in ChromaDB
            # ---------------------------------
            vector_store.add_document_chunks(document_chunks)

            # ---------------------------------
            # Console Output
            # ---------------------------------
            print(f"\n========== {file.filename} ==========")
            print(f"Total Chunks          : {len(document_chunks)}")

            if document_chunks:
                print(
                    f"Embedding Dimension  : "
                    f"{len(document_chunks[0].embedding)}"
                )

            print(
                f"Documents in ChromaDB: "
                f"{vector_store.count_documents()}"
            )

            print("\nFirst 3 Chunks:\n")

            for chunk in document_chunks[:3]:

                print(f"Chunk Index : {chunk.chunk_index}")
                print(f"Page Number : {chunk.page_number}")
                print("-" * 60)
                print(chunk.text[:300])
                print()

            print("=" * 60)

            uploaded_files.append(file.filename)

        return UploadResponse(
            message="PDFs uploaded successfully.",
            files_uploaded=len(uploaded_files),
            filenames=uploaded_files
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# ==========================================
# Chat Endpoint
# ==========================================

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    return ChatResponse(
        answer="Chat endpoint is working. Semantic search will be implemented next.",
        sources=[]
    )