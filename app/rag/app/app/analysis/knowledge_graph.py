import requests


def extract_knowledge(context):

    prompt = f"""
Analiza el texto y extrae relaciones de políticas públicas.

Devuelve una lista en formato:

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

    return result["response"]
    