from fastapi import FastAPI
from backend.api import chat, user, portfolio
from db.mongo import MongoDB
import os 

# Initialize MongoDB connection 
MongoDB(uri=os.getenv('MONGO_URI'))

app = FastAPI()

app.include_router(chat.router, prefix="/api")
app.include_router(user.router, prefix="/api")
app.include_router(portfolio.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Robo-Advisor MVP API"} 