from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from app.agent.orchestrator import run_agent
from starlette.websockets import WebSocketDisconnect
import time
from app.agent.reminder import start_reminder_loop
from app.logger import log_request, log_response
import time

start_reminder_loop()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

current_task = None

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"status": "running 🚀"}

from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("🔌 WebSocket connected")

    while True:
        try:
            msg = await websocket.receive_text()
            print("📡 INPUT:", msg)

            reply = f"Echo: {msg}"
            await websocket.send_text(reply)

        except Exception as e:
            print("❌ WebSocket error:", e)
            break

    except Exception as e:
        print("ERROR:", e)
