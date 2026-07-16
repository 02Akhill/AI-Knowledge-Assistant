# Import BaseModel for API responses
from pydantic import BaseModel


# Response returned after uploading PDFs
class UploadResponse(BaseModel):
    message: str
    files_uploaded: int
    filenames: list[str]