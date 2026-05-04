import json
from langchain.tools import tool

def load_doctors():
    with open("data/doctors.json", "r", encoding="utf-8") as f:
        return json.load(f)["doctors"]

@tool
def doctor_finder_tool(specialty: str) -> str:
    """
    Finds available doctors based on a medical specialty.
    Use this after identifying the required specialty from symptoms.
    Input: a medical specialty (e.g. 'Cardiologue', 'Généraliste').
    Output: list of available doctors matching that specialty.
    """
    doctors = load_doctors()
    specialty_lower = specialty.lower()

    matches = [
        d for d in doctors
        if specialty_lower in d["specialty"].lower() and d["available"]
    ]

    if not matches:
        # fallback to general practitioner
        matches = [
            d for d in doctors
            if "généraliste" in d["specialty"].lower() and d["available"]
        ]
        return f"Aucun spécialiste trouvé pour '{specialty}'.\nMédecin généraliste disponible:\n" + \
               "\n".join([f"- {d['name']} (ID: {d['id']})" for d in matches])

    result = f"Médecins disponibles pour '{specialty}':\n"
    result += "\n".join([f"- {d['name']} (ID: {d['id']})" for d in matches])
    return result