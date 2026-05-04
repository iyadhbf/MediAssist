import json
from langchain.tools import tool

CALENDAR_PATH = "data/calendar.json"

def load_calendar():
    with open(CALENDAR_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_calendar(data):
    with open(CALENDAR_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

@tool
def appointment_tool(doctor_id: str) -> str:
    """
    Books the first available appointment slot for a given doctor.
    Use this after the user confirms they want to book with a specific doctor.
    Input: the doctor's ID as a string (e.g. '1', '2').
    Output: booking confirmation with date and time, or unavailability message.
    """
    data = load_calendar()
    slots = data["slots"]

    try:
        doc_id = int(doctor_id)
    except ValueError:
        return "ID médecin invalide. Veuillez fournir un numéro."

    available = [
        s for s in slots
        if s["doctor_id"] == doc_id and not s["booked"]
    ]

    if not available:
        return f"Aucun créneau disponible pour le médecin ID {doc_id}."

    # Book the first available slot
    slot = available[0]
    slot["booked"] = True
    save_calendar(data)

    return (
        f"✅ Rendez-vous confirmé!\n"
        f"📅 Date: {slot['date']}\n"
        f"⏰ Heure: {slot['time']}\n"
        f"🏥 Médecin ID: {doc_id}"
    )