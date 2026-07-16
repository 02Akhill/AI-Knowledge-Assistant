# FastAPI imports
from fastapi import FastAPI, UploadFile, File, HTTPException

# Response model
from backend.models import UploadResponse

# File service
from backend.services.file_service import save_pdf, extract_text

# Chunk service
from backend.services.chunk_service import create_chunks

# Gemini service
from backend.services.gemini_service import create_embeddings


# Create FastAPI app
app = FastAPI(
    title="AI Knowledge Assistant",
    version="0.5"
)


# Home Endpoint
@app.get("/")
def home():
    return {
        "message": "AI Knowledge Assistant is running."
    }


# Upload Multiple PDFs
@app.post("/upload", response_model=UploadResponse)
async def upload_pdfs(files: list[UploadFile] = File(...)):

    uploaded_files = []

    try:

        for file in files:

            # Save PDF
            pdf_path = await save_pdf(file)

            # Extract text from PDF
            text = extract_text(pdf_path)

            # Create chunks
            chunks = create_chunks(text)

            # Generate Gemini embeddings
            embeddings = create_embeddings(chunks)

            # Display information
            print("\n" + "=" * 70)
            print(f"File : {file.filename}")
            print("=" * 70)

            print(f"Total Chunks       : {len(chunks)}")
            print(f"Total Embeddings   : {len(embeddings)}")

            if len(embeddings) > 0:
                print(
                    f"Embedding Dimension : {len(embeddings[0].values)}"
                )

            print("\nFirst Three Chunks")

            for index, chunk in enumerate(chunks[:3], start=1):

                print(f"\nChunk {index}")
                print("-" * 50)
                print(chunk[:300])

            print("=" * 70)

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