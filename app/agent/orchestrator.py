from app.memory.memory import get_session, set_session
from app.agent.tools import (
    book_appointment,
    cancel_appointment,
    check_availability
)

# -----------------------------
# MOCK INTENT ENGINE
# -----------------------------
def mock_llm(user_input, session):

    text = user_input.lower()

    # BOOKING
    if "book" in text or "appointment" in text:

        doctor = "Dr Rao"
        time = "tomorrow"

        if "smith" in text:
            doctor = "Dr Smith"
        elif "mehta" in text:
            doctor = "Dr Mehta"

        return {
            "intent": "book",
            "doctor": doctor,
            "time": time,
            "response": f"Booking appointment with {doctor}."
        }

    # CANCEL
    if "cancel" in text:

        return {
            "intent": "cancel",
            "doctor": session.get("doctor", "Dr Rao"),
            "time": session.get("time", "tomorrow"),
            "response": "Cancelling your appointment."
        }

    # CHECK
    if "available" in text:

        return {
            "intent": "check",
            "doctor": "Dr Rao",
            "time": "tomorrow",
            "response": "Checking availability."
        }

    # DEFAULT
    return {
        "intent": None,
        "response": "I can help you book, cancel, or check appointments."
    }


# -----------------------------
# MAIN ORCHESTRATOR
# -----------------------------
def run_agent(user_input: str, session_id: str):

    # 1. LOAD MEMORY
    session = get_session(session_id) or {}

    # 2. INTENT DETECTION
    result = mock_llm(user_input, session)

    intent = result["intent"]
    response_text = result["response"]

    tool_result = ""

    # 3. TOOL EXECUTION
    if intent == "book":
        tool_result = book_appointment("p1", result["doctor"], result["time"])

        session["doctor"] = result["doctor"]
        session["time"] = result["time"]

    elif intent == "cancel":
        tool_result = cancel_appointment(result["doctor"], result["time"])

    elif intent == "check":
        tool_result = check_availability(result["doctor"], result["time"])

    else:
        tool_result = response_text

    # 4. MEMORY UPDATE (FINAL CONSISTENT STATE)
    session["last_input"] = user_input
    session["last_intent"] = intent
    session["last_tool_result"] = tool_result
    session["turn_count"] = session.get("turn_count", 0) + 1

    set_session(session_id, session)

    # 5. RESPONSE
    return f"{response_text}\n\n{tool_result}"

    print("🤖 FINAL RESPONSE:", final_response)

    return final_response