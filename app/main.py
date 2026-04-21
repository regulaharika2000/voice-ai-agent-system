from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.get("/")
def health():
    return {"status": "running"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("🔌 Connected")

    while True:
        try:
            msg = await websocket.receive_text()
            print("📡 INPUT:", msg)

            reply = f"Echo: {msg}"
            await websocket.send_text(reply)

        except Exception as e:
            print("❌ Error:", e)
            break
