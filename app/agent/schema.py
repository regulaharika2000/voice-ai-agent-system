tools = [
    {
        "type": "function",
        "function": {
            "name": "book_appointment",
            "description": "Book a clinical appointment",
            "parameters": {
                "type": "object",
                "properties": {
                    "patient_id": {"type": "string"},
                    "doctor": {"type": "string"},
                    "time": {"type": "string"}
                },
                "required": ["patient_id", "doctor", "time"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "cancel_appointment",
            "description": "Cancel an appointment",
            "parameters": {
                "type": "object",
                "properties": {
                    "doctor": {"type": "string"},
                    "time": {"type": "string"}
                },
                "required": ["doctor", "time"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "check_availability",
            "description": "Check doctor availability",
            "parameters": {
                "type": "object",
                "properties": {
                    "doctor": {"type": "string"},
                    "time": {"type": "string"}
                },
                "required": ["doctor", "time"]
            }
        }
    }
]