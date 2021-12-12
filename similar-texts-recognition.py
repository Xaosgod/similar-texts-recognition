from fastapi import FastAPI, File, UploadFile
from typing import List
import difflib
app = FastAPI()

@app.post("/similar-recognition")
async def create_upload_files(files: List[UploadFile] = File(...)):
  text1 = await files[0].read()
  text2 = await files[1].read()
  normalized1 = text1.lower()
  normalized2 = text2.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()
  
    



