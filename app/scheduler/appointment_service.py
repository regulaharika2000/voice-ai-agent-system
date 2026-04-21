from app.scheduler.doctor_db import DOCTORS

appointments = []

def book_appointment(doctor, time):

    if doctor not in DOCTORS:
        return "Doctor not found"

    if time not in DOCTORS[doctor]:
        return "Slot not available"

    if (doctor, time) in appointments:
        return "Already booked"

    appointments.append((doctor, time))
    return f"Booked {doctor} at {time}"