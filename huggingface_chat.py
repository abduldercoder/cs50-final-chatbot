import requests
import os
from dotenv import load_dotenv

load_dotenv()
HUGGINGFACE_API_TOKEN = os.getenv("HF_TOKEN")

def hf_response(prompt):
    url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

    # Offiziell braucht DialoGPT eigentlich "past_user_inputs" und "generated_responses" 
    # wenn man einen längeren Dialog führt, aber für eine einfache Antwort reicht das hier:
    payload = {
        "inputs": {
            "past_user_inputs": [],
            "generated_responses": [],
            "text": prompt
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        print("DEBUG RESULT:", result)

        # Normalerweise kommt so was wie {"generated_text": "..."}
        # Manchmal ist es ein dict, manchmal ein list. Wir handlen beides:
        if isinstance(result, dict) and "generated_text" in result:
            return result["generated_text"].strip()

        if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
            return result[0]["generated_text"].strip()

        return "(Modell hat keine sinnvolle Antwort geliefert)"
    except Exception as e:
        print("Fehler bei API:", e)
        print("Antwort:", response.text)
        return f"(Fehler mit Hugging Face API: {e})"
