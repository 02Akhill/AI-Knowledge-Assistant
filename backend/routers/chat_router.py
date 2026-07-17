from fastapi import APIRouter

from backend.models import ChatRequest, ChatResponse


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):

    return ChatResponse(
        answer="Chat endpoint is working. Semantic search will be implemented next.",
        sources=[]
    )