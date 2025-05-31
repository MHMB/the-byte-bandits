def send_message_to_chat_api(message):
    import requests

    url = "http://backend:8000/api/chat"
    payload = {"message": message, "username": "1"}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get("response")
    else:
        return "Error: Unable to get a response from the chatbot API."