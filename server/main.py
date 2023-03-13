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

app.mount('/api', web_socket_app)
app.mount("/", StaticFiles(directory="web_root", html=True), name="web_root")
