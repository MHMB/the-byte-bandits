from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from backend.llm.conversation_manager import ConversationManager
from backend.llm.assistant import Assistant
from backend.llm.openai_client import OpenAIClient
from backend.api.models.chat_model import ChatRequest, ChatResponse

router = APIRouter()

conversation_manager = ConversationManager()
assistant = Assistant(instructions_path="backend/llm/instructions.txt")
openai_client = OpenAIClient()

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    user_message = request.message
    user_id = request.username
    if not user_message:
        return JSONResponse({"error": "No message provided."}, status_code=400)

    history = conversation_manager.get_history(user_id)
    if not history:
        # First message: inject system prompt
        system_prompt = assistant.get_system_prompt()
        initial_messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
        conversation_manager.create_history(user_id, initial_messages)
        history = initial_messages
    else:
        # Continue conversation
        conversation_manager.append_message(user_id, {"role": "user", "content": user_message})
        history = conversation_manager.get_history(user_id)

    functions = assistant.get_function_definitions()
    response = openai_client.chat_completion(messages=history, functions=functions)
    assistant_reply = response.choices[0].message.content if response.choices else ""
    conversation_manager.append_message(user_id, {"role": "assistant", "content": assistant_reply})
    return {"response": assistant_reply} 