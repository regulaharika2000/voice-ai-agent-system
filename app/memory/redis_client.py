import json

SESSION_STORE = {}


def get_session(session_id: str):
    return SESSION_STORE.get(session_id, {})


def set_session(session_id: str, data: dict, ttl: int = 1800):
    SESSION_STORE[session_id] = data