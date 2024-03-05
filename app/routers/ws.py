import logging

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.core.ws_manager import connection_manager

router = APIRouter(prefix="/ws", tags=["Websocket"])
logger = logging.getLogger(__name__)


@router.websocket("/{email}")
async def websocket_endpoint(websocket: WebSocket, email: str):
    await connection_manager.connect(websocket, email)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        connection_manager.disconnect(websocket)
