from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from backend.llm.conversation_manager import ConversationManager

router = APIRouter()

conversation_manager = ConversationManager()

@router.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_message = data.get("message")
    if not user_message:
        return JSONResponse({"error": "No message provided."}, status_code=400)

    # Simple chat history: system prompt + user message
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message}
    ]
    assistant_reply = conversation_manager.send_message(messages)
    return {"response": assistant_reply} 