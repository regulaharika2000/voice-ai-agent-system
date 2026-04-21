from datetime import datetime, timedelta

# -------------------------
# DOCTOR CALENDARS
# -------------------------
doctor_calendar = {
    "Dr Rao": [],
    "Dr Smith": [],
    "Dr Mehta": []
}


# -------------------------
# PARSE SIMPLE TIME
# -------------------------
def parse_time(time_str):
    """
    VERY SIMPLE parser (Phase 5 starter version)
    """
    if "tomorrow" in time_str.lower():
        base = datetime.now() + timedelta(days=1)
        return base.replace(hour=10, minute=0, second=0)

    if "today" in time_str.lower():
        return datetime.now().replace(minute=0, second=0)

    # default fallback
    return datetime.now() + timedelta(hours=1)


# -------------------------
# CHECK SLOT
# -------------------------
def is_available(doctor, slot_time):
    if doctor not in doctor_calendar:
        return False

    for booked in doctor_calendar[doctor]:
        if abs((booked - slot_time).total_seconds()) < 1800:  # 30 min gap
            return False

    return True


# -------------------------
# FIND NEXT SLOT
# -------------------------
def suggest_slot(doctor):
    base = datetime.now() + timedelta(hours=1)

    for i in range(1, 10):
        candidate = base + timedelta(minutes=30 * i)
        if is_available(doctor, candidate):
            return candidate

    return None


# -------------------------
# BOOK SLOT
# -------------------------
def book_slot(doctor, time_str):

    slot_time = parse_time(time_str)

    if doctor not in doctor_calendar:
        return "❌ Doctor not found"

    if is_available(doctor, slot_time):
        doctor_calendar[doctor].append(slot_time)
        return f"✅ Booked with {doctor} at {slot_time.strftime('%Y-%m-%d %H:%M')}"

    # conflict → suggest alternative
    suggestion = suggest_slot(doctor)

    if suggestion:
        return f"❌ Slot busy. Next available: {suggestion.strftime('%Y-%m-%d %H:%M')}"

    return "❌ No slots available"


# -------------------------
# CANCEL SLOT
# -------------------------
def cancel_slot(doctor, time_str):
    slot_time = parse_time(time_str)

    if doctor in doctor_calendar:
        doctor_calendar[doctor] = [
            t for t in doctor_calendar[doctor]
            if abs((t - slot_time).total_seconds()) > 60
        ]
        return "✅ Appointment cancelled"

    return "❌ Doctor not found"