from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_allowed_origins
from app.routes import router


app = FastAPI(
    title="Agentic AI Customer Support Assistant",
    description="A production-style customer support assistant using FastAPI, LangChain agents, custom tools, memory, and Groq LLM.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Agentic AI Customer Support Assistant API",
        "docs": "/docs",
        "chat_endpoint": "/api/support/chat",
    }