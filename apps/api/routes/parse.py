from fastapi import APIRouter, UploadFile
from services import pdf_parser

router = APIRouter()

@router.post("/pdf")
async def parse_pdf(file: UploadFile):
    text = await pdf_parser.extract_text_from_pdf(file)
    return {"text": text}