import time
import uuid


def log_request(user_input, session_id):
    trace_id = str(uuid.uuid4())[:8]

    print("\n" + "="*60)
    print(f"🧠 TRACE ID: {trace_id}")
    print(f"📥 INPUT: {user_input}")
    print(f"🆔 SESSION: {session_id}")
    print(f"⏰ TIME: {time.strftime('%H:%M:%S')}")
    print("-"*60)

    return trace_id


def log_response(trace_id, response, latency):

    status = "OK" if latency < 450 else "SLOW"

    print(f"📤 OUTPUT: {response}")
    print(f"⏱ LATENCY: {latency:.2f} ms [{status}]")
    print(f"🔖 TRACE ID: {trace_id}")
    print("="*60 + "\n")