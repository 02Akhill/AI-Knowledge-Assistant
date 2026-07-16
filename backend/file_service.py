# Work with folders
from pathlib import Path

# FastAPI upload type
from fastapi import UploadFile

# PDF library
import fitz


# Upload folder
UPLOAD_FOLDER = Path("data/uploads")

# Create folder automatically
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


# Save one PDF
async def save_pdf(file: UploadFile) -> str:

    if not file.filename.lower().endswith(".pdf"):
        raise ValueError(f"{file.filename} is not a PDF.")

    file_path = UPLOAD_FOLDER / file.filename

    file_path.write_bytes(await file.read())

    return str(file_path)


# Extract text from one PDF
def extract_text(pdf_path: str) -> str:

    with fitz.open(pdf_path) as document:

        text = ""

        for page in document:
            text += page.get_text()

    return text.strip()