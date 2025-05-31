from fastapi import APIRouter
from fastapi.responses import JSONResponse
from llm.conversation_manager import ConversationManager
from llm.assistant import Assistant
from llm.openai_client import OpenAIClient
from api.models.chat_model import ChatRequest, ChatResponse
from llm.functions.function_manager import FunctionFactory
import json
import logging

router = APIRouter()

conversation_manager = ConversationManager()
assistant = Assistant(instructions_path="./llm/instructions.txt")
openai_client = OpenAIClient()

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    user_message = request.message
    user_id = request.username
    if not user_message:
        return JSONResponse({"error": "No message provided."}, status_code=400)

    history = conversation_manager.get_history(user_id)
    # logging.warning("History: %s", history)
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

    # Function call loop
    while True:
        logging.warn("Sending messages to OpenAI: %s", json.dumps(history, ensure_ascii=False))
        response = openai_client.chat_completion(messages=history, functions=functions)
        choice = response.choices[0].message if response.choices else None
        if not choice:
            assistant_reply = "مشکلی پیش آمده است. لطفاً دوباره تلاش کنید."
            conversation_manager.append_message(user_id, {"role": "assistant", "content": assistant_reply})
            return {"response": assistant_reply}

        # Check for function call
        if hasattr(choice, "function_call") and choice.function_call:
            function_call = choice.function_call
            function_name = function_call.name
            function_args = json.loads(function_call.arguments) if function_call.arguments else {}
            # Execute the function
            try:
                func_cls = FunctionFactory.get_function(function_name)
                if hasattr(func_cls, "run") and callable(getattr(func_cls, "run")):
                    result = func_cls.run(function_call_args=function_args)
                else:
                    result = (None, "Function not implemented correctly.")
                function_response = result[1] if isinstance(result, tuple) else str(result)
            except Exception as e:
                function_response = f"Function execution error: {str(e)}"
            # Append function call and result to history
            history.append({
                "role": "function",
                "name": function_name,
                "content": function_response
            })
            conversation_manager.set_history(user_id, history)
            # Continue loop: send updated history to OpenAI
            continue
        else:
            # Normal assistant message
            assistant_reply = choice.content or ""
            conversation_manager.append_message(user_id, {"role": "assistant", "content": assistant_reply})
            return {"response": assistant_reply} 