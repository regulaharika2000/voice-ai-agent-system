from fastapi import APIRouter, WebSocket
from app.agent.agent_loop import AgentLoop

router = APIRouter()
agent = AgentLoop()

@router.websocket("/ws/audio")
async def audio_stream(ws: WebSocket):
    await ws.accept()

    while True:
        data = await ws.receive_text()

        response = await agent.handle_text(data)

        await ws.send_text(response)