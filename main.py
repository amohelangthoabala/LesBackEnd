print("import dependencies...")
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from interface.routes import users, authentication, message, chat, websocket
from infrastructure.orm.sqlalchemy import models
from infrastructure.database.database import engine
from infrastructure.websocket.WebsocketConnectionManager import WebsocketConnectionManager

app = FastAPI()

app.mount("/", StaticFiles(directory="interface/static",html = True), name="static")

models.Base.metadata.create_all(engine)
#models.Base.metadata.drop_all(engine)

from fastapi.responses import HTMLResponse



manager = WebsocketConnectionManager()


# @app.get('/')
# async def home():
#     return HTMLResponse(html)

@app.websocket("/websocket/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")

app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(chat.router)
app.include_router(message.router)
# app.include_router(websocket.router)

print("running...")
