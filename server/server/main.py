from fastapi import FastAPI, WebSocket
from random import random
import asyncio

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.websocket("/ws")
async def ws_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        #data = await websocket.receive_text()
        #print(f"Received: {data} from websocket")


        while True:
            num = random()
            p = websocket.send_text(str(num))
            await asyncio.sleep(1)
            await p


