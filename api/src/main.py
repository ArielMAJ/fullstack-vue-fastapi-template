import asyncio
from random import random

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import Config
from src.schemas.random_response import RandomResponse
from src.schemas.root_response import RootResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_model=RootResponse)
async def root():
    await asyncio.sleep(random() * 7)
    return {"message": "Hello World message from the back-end!"}


@app.get("/random", response_model=RandomResponse)
async def random_number():
    seconds = random() * 5
    await asyncio.sleep(seconds)
    return {"message": round(seconds, 2)}


if __name__ == "__main__":
    uvicorn.run("src.main:app", host=Config.HOST, port=Config.PORT, reload=True)
