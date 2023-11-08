from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

app = FastAPI()


class Message(BaseModel):
    text: str


@app.post("/")
async def completeChat(message: Message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."}, {
            "role": "user", "content": message.text}]
    )
    return {"message": response.choices[0].message.content}
