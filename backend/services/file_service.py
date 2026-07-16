# Work with folders
from pathlib import Path

# FastAPI upload type
from fastapi import UploadFile

# PDF library
import fitz

# Models
from backend.models import DocumentPage


# Upload folder
UPLOAD_FOLDER = Path("data/uploads")

# Create folder automatically
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


# ------------------------------------------
# Save one PDF
# ------------------------------------------
async def save_pdf(file: UploadFile) -> str:

    if not file.filename.lower().endswith(".pdf"):
        raise ValueError(f"{file.filename} is not a PDF.")

    file_path = UPLOAD_FOLDER / file.filename

    file_path.write_bytes(await file.read())

    return str(file_path)


# ------------------------------------------
# Old function
# Keep for backward compatibility
# ------------------------------------------
def extract_text(pdf_path: str) -> str:

    pages = extract_pages(pdf_path)

    return "\n".join(page.text for page in pages).strip()


# ------------------------------------------
# New function
# Extract page-by-page
# ------------------------------------------
def extract_pages(pdf_path: str) -> list[DocumentPage]:

    document_pages: list[DocumentPage] = []

    with fitz.open(pdf_path) as pdf:

        for page_number, page in enumerate(pdf, start=1):

            text = page.get_text().strip()

            if not text:
                continue

            document_pages.append(
                DocumentPage(
                    page_number=page_number,
                    text=text
                )
            )

    return document_pages