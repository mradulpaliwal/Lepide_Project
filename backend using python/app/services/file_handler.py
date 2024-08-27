# app/services/file_handler.py
import os
from pathlib import Path
from fastapi import UploadFile

UPLOAD_DIR = "uploads/"

async def save_file(file: UploadFile) -> str:
    file_path = Path(UPLOAD_DIR) / file.filename
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return str(file_path)

def get_file_content(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1]
    if ext == '.txt':
        with open(file_path, 'r') as f:
            return f.read()
    # Add logic for reading PDFs and DOCX files
