from fastapi import FastAPI, WebSocket, Request
from fastapi.middleware.cors import CORSMiddleware
from random import random
import asyncio
from sse_starlette.sse import EventSourceResponse

app = FastAPI()

origins = [
    #"http://localhost:3000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.get("/sse")
async def sse_endpoint(request: Request):

    async def event_source():
        while True:

            if await request.is_disconnected():
                break

            await asyncio.sleep(1)
            yield random()

    return EventSourceResponse(event_source())
