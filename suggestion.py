from fastapi import FastAPI
import json
import random


app = FastAPI()

# loading messages
with open("messages.json", "r", encoding="utf-8") as f:
    messages = json.load(f)

@app.get("/suggestion")
def get_motivation():
    return random.choice(messages)