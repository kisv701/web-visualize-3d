import asyncio

from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles


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
        mocked_data = {
            'x': [1, 2, 3, 4],
            'y': [1, 2, 3, 4],
            'z': [1, 2, 3, 4],
            'r': [1, 2, 3, 4],
            'g': [1, 2, 3, 4],
            'b': [1, 2, 3, 4],
        }
        await websocket.send_json(mocked_data)
        await asyncio.sleep(2)

app.mount('/api', web_socket_app)
app.mount("/", StaticFiles(directory="web_root", html=True), name="web_root")
