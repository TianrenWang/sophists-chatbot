from fastapi import APIRouter, Request
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

router = APIRouter()


class Message(BaseModel):
    text: str


@router.post("/")
async def chat(message: Message, request: Request):
    print(request.state.current_user)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."}, {
            "role": "user", "content": "Hey this is " + request.state.current_user.full_name + " " + message.text}]
    )
    return {"message": response.choices[0].message.content}
