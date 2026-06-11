from fastapi import APIRouter, HTTPException

from app.agent_service import run_support_agent
from app.memory_store import memory_store
from app.schemas import SupportChatRequest, SupportChatResponse

router = APIRouter()


@router.get("/health")
async def health_check():
    return {
        "status": "ok",
        "message": "Customer support assistant API is running",
    }


@router.post("/support/chat", response_model=SupportChatResponse)
async def support_chat(request: SupportChatRequest):
    try:
        response = await run_support_agent(
            message=request.message,
            session_id=request.session_id,
        )
        return SupportChatResponse(response=response, session_id=request.session_id)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process support request: {str(exc)}",
        )


@router.delete("/support/chat/{session_id}")
async def clear_chat_memory(session_id: str):
    memory_store.clear_history(session_id)
    return {
        "status": "success",
        "message": f"Memory cleared for session {session_id}",
    }