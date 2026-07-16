# Import Path for working with folders
from pathlib import Path

# Import UploadFile from FastAPI
from fastapi import UploadFile

# Folder where uploaded files will be stored
UPLOAD_FOLDER = Path("data")

# Create the folder automatically if it doesn't exist
UPLOAD_FOLDER.mkdir(exist_ok=True)


# Save uploaded PDF
async def save_pdf(file: UploadFile) -> str:
    # Allow only PDF files
    if not file.filename.lower().endswith(".pdf"):
        raise ValueError("Only PDF files are allowed.")

    # Create complete file path
    file_path = UPLOAD_FOLDER / file.filename

    # Read uploaded file
    content = await file.read()

    # Save file to disk
    file_path.write_bytes(content)

    # Return saved filename
    return file.filename