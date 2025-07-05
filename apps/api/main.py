from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import parse, chat, ocr

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(parse.router, prefix="/parse")
app.include_router(chat.router, prefix="/chat")
app.include_router(ocr.router, prefix="/ocr")

@app.get("/")
def read_root():
    return {"message": "ScholarGenie API is running"}