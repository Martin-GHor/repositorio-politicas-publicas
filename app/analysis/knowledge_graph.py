import requests

def extract_relations(context):
    prompt = f'Extrae relaciones del texto sobre políticas públicas.\n\nDevuelve SOLO líneas con formato:\n\nACTOR | RELACION | CONCEPTO\n\nTexto:\n{context}'
    
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json().get("response", "")
    except Exception as e:
        return f"Error: {e}"
