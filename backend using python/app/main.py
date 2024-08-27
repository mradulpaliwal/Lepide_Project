# app/main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from app.services.file_handler import save_file, get_file_content
from app.services.summarizer import summarize_document
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_path = await save_file(file)
        return {"filename": file.filename, "file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/summarize")
async def summarize(file_path: str):
    try:
        content = get_file_content(file_path)
        summary = summarize_document(content)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




/#Usage of configuration if needed

#from app.config import settings

#@app.post("/upload")
#async def upload_file(file: UploadFile = File(...)):
    # Use settings to get the upload directory
    #file_path = await save_file(file, settings.upload_dir)
   # return {"filename": file.filename, "file_path": file_path}
