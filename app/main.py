from fastapi import Depends, FastAPI

from .routers import index, token
from .dependencies import get_current_active_user

app = FastAPI()
app.include_router(token.router, prefix="/token",
                   tags=["token"])
app.include_router(index.router, prefix="/api",
                   dependencies=[Depends(get_current_active_user)])


@app.post("/")
async def completeChat():
    return {"message": "You are in the house of Terran"}
