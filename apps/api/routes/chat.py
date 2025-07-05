from fastapi import APIRouter, Body
from services import summarizer

router = APIRouter()

@router.post("/explain")
async def explain_text(payload: dict = Body(...)):
    query = payload.get("query")
    mode = payload.get("mode", "normal")
    result = summarizer.get_explanation(query, mode)
    return {"response": result}