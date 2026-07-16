# FastAPI imports
from fastapi import FastAPI, UploadFile, File, HTTPException

# Response model
from backend.models import UploadResponse

# File functions
from backend.file_service import save_pdf, extract_text
from backend.chunk_service import create_chunks


# Create app
app = FastAPI(
    title="AI Knowledge Assistant",
    version="0.3"
)


# Home endpoint
@app.get("/")
def home():

    return {
        "message": "AI Knowledge Assistant is running."
    }


# Upload multiple PDFs
@app.post("/upload", response_model=UploadResponse)
async def upload_pdfs(files: list[UploadFile] = File(...)):

    uploaded_files = []

    try:

        for file in files:

            # Save PDF
            pdf_path = await save_pdf(file)

            # Read text
            text = extract_text(pdf_path)

            # Split into chunks
            chunks = create_chunks(text)

            print(f"\n========== {file.filename} ==========")
            print(f"Total Chunks : {len(chunks)}")

            # Print first three chunks
            for index, chunk in enumerate(chunks[:3], start=1):

                print(f"\nChunk {index}")
                print("-" * 40)
                print(chunk[:300])

            print("=====================================\n")

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