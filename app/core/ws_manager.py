from typing import List

from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket, email: str):
        await websocket.accept()
        self.active_connections.append((email, websocket))

    def disconnect(self, websocket: WebSocket):
        for index, (email, ws) in enumerate(self.active_connections):
            if ws == websocket:
                self.active_connections.pop(index)
                break

    async def send_personal_message(self, message: str, recipient: str):
        for email, ws in self.active_connections:
            if email == recipient:
                await ws.send_text(message)

    async def broadcast_message(self, message: str):
        for _, ws in self.active_connections:
            await ws.send_text(message)


connection_manager = ConnectionManager()
