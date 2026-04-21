SESSION_STORE = {}


def get_session(session_id):
    return SESSION_STORE.get(session_id, {})


def set_session(session_id, data):
    SESSION_STORE[session_id] = data