from fastapi import APIRouter, UploadFile
from services import ocr_engine

router = APIRouter()

@router.post("/image")
async def ocr_image(file: UploadFile):
    text = await ocr_engine.extract_text_from_image(file)
    return {"text": text}