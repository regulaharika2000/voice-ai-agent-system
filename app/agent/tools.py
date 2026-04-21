from app.agent.scheduler import book_slot, cancel_slot


def book_appointment(patient_id, doctor, time):
    return book_slot(doctor, time)


def cancel_appointment(doctor, time):
    return cancel_slot(doctor, time)


def check_availability(doctor, time):
    from app.agent.scheduler import is_available, parse_time

    slot = parse_time(time)
    return "Available" if is_available(doctor, slot) else "Not available"