from fastapi import FastAPI
from backend.api import chat, user, portfolio

app = FastAPI()

app.include_router(chat.router, prefix="/api")
app.include_router(user.router, prefix="/api")
app.include_router(portfolio.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Robo-Advisor MVP API"} 