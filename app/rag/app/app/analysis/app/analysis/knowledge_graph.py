import requests


def extract_relations(context):

    prompt = f"""
Extrae relaciones del texto sobre políticas públicas.

Devuelve SOLO líneas con formato:

ACTOR | RELACION | CONCEPTO

Texto:
{context}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    relations = result["response"]

    return relations
    exit