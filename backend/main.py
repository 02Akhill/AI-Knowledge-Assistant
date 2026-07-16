# FastAPI imports
from fastapi import FastAPI, UploadFile, File, HTTPException

# Response model
from backend.models import UploadResponse

# File functions
from backend.file_service import save_pdf, extract_text


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

            print(f"\n========== {file.filename} ==========")
            print(text[:500])
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