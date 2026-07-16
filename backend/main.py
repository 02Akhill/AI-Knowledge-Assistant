# FastAPI imports
from fastapi import FastAPI, UploadFile, File, HTTPException

# Import response model
from backend.models import UploadResponse

# Import upload service
from backend.file_service import save_pdf

# Create FastAPI application
app = FastAPI(
    title="AI Knowledge Assistant",
    version="1.0.0"
)


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "AI Knowledge Assistant is running."
    }


# Upload endpoint
@app.post("/upload", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):
    try:
        # Save uploaded PDF
        filename = await save_pdf(file)

        # Return success response
        return UploadResponse(
            message="PDF uploaded successfully.",
            filename=filename
        )

    except ValueError as error:
        # Return validation error
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )