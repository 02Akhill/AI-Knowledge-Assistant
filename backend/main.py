# FastAPI imports
from fastapi import FastAPI, UploadFile, File, HTTPException

# Response model
from backend.models import UploadResponse

# Services
from backend.services.file_service import save_pdf
from backend.services.document_service import process_document
from backend.services.gemini_service import create_embeddings


# Create FastAPI app
app = FastAPI(
    title="AI Knowledge Assistant",
    version="0.5"
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

            # -------------------------------
            # Save PDF
            # -------------------------------
            pdf_path = await save_pdf(file)

            # -------------------------------
            # Process Document
            # -------------------------------
            document_chunks = process_document(
                pdf_path=pdf_path,
                document_name=file.filename
            )

            # -------------------------------
            # Generate Embeddings
            # -------------------------------
            document_chunks = create_embeddings(document_chunks)

            # -------------------------------
            # Print Information
            # -------------------------------
            print(f"\n========== {file.filename} ==========")
            print(f"Total Chunks : {len(document_chunks)}")

            if document_chunks:

                print(
                    f"Embedding Dimension : "
                    f"{len(document_chunks[0].embedding)}"
                )

            # Print first 3 chunks
            for chunk in document_chunks[:3]:

                print(f"\nChunk {chunk.chunk_index}")
                print(f"Page : {chunk.page_number}")
                print("-" * 40)
                print(chunk.text[:300])

            print("\n=====================================\n")

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