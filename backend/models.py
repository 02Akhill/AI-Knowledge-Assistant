# Import BaseModel for creating API response models
from pydantic import BaseModel


# Response returned after a successful upload
class UploadResponse(BaseModel):
    message: str
    filename: str