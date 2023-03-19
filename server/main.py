import asyncio
import time
import math

from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from .mock_elements import generate_box


app = FastAPI()
web_socket_app = FastAPI()


@web_socket_app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

@web_socket_app.websocket("/point_cloud")
async def point_cloud_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        scale = 2 + math.sin(time.time() * 0.33 * math.pi)
        mocked_data = generate_box(scale)
        await websocket.send_json(mocked_data)
        await asyncio.sleep(1/60)

app.mount('/api', web_socket_app)
app.mount("/", StaticFiles(directory="web_root", html=True), name="web_root")
