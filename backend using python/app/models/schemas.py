# app/models/schemas.py

from pydantic import BaseModel

# Response model for file upload
class FileUploadResponse(BaseModel):
    filename: str
    file_path: str

# Request model for summarization
class SummarizeRequest(BaseModel):
    file_path: str

# Response model for summarization
class SummarizeResponse(BaseModel):
    summary: str
