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

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:

            msg = await websocket.receive_text()

            trace_id = log_request(msg, "session1")

            start = time.perf_counter()

            reply = run_agent(msg, session_id="session1")

            await websocket.send_text(reply)

            end = time.perf_counter()

            latency = (end - start) * 1000

            log_response(trace_id, reply, latency)

    except Exception as e:
        print("ERROR:", e)
