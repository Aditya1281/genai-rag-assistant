from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

from app.services.rag import rag_pipeline
from app.init_index import initialize_index

app = FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

initialize_index()

class ChatRequest(BaseModel):

    sessionId: str
    message: str

@app.get("/")
def home():

    return {
        "message": "RAG API Running"
    }

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }

@app.post("/api/chat")
def chat(request: ChatRequest):

    response = rag_pipeline(
        request.message,
        request.sessionId
    )

    return response