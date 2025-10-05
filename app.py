from fastapi import FastAPI
from pydantic import BaseModel
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="LLM Backend")

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_text(request: PromptRequest):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": request.prompt}],
        max_tokens=300,
        temperature=0.7
    )
    text = response.choices[0].message["content"].strip()
    return {"response": text}

@app.get("/")
def read_root():
    return {"message": "LLM Backend is running!"}
