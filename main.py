from fastapi import FastAPI
from chatbot import create_chat_engine

app = FastAPI()

chat_engine = create_chat_engine()

@app.get("/")
def home():
    return {
        "message": "AI Knowledge Chatbot Running"
    }

@app.get("/chat")
def chat(query: str):

    response = chat_engine.chat(query)

    return {
        "answer": str(response)
    }