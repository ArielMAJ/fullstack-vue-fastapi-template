import asyncio
from random import random

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
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
    logger.debug(f"Sleeping for {seconds} seconds before answering request.")
    await asyncio.sleep(seconds)
    return {"message": round(seconds, 2)}


@app.get("/health")
def health():
    return {"status": "alive"}


if __name__ == "__main__":
    uvicorn.run("src.main:app", port=Config.PORT, reload=False)
