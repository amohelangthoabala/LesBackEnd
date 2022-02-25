print("import dependencies...")
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from interface.routes import users, authentication, message, chat, websocket
from infrastructure.orm.sqlalchemy import models
from infrastructure.database.database import engine
from infrastructure.websocket.WebsocketConnectionManager import WebsocketConnectionManager

app = FastAPI()
print("app strating...")

models.Base.metadata.create_all(engine)
# #models.Base.metadata.drop_all(engine)

from fastapi.responses import HTMLResponse

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:8000/websocket/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""



manager = WebsocketConnectionManager()


@app.get('/')
async def home():
    return HTMLResponse(html)

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
