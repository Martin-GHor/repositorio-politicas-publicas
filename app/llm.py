
from app.memory import get_memory, add_to_memory
import ollama

def generar_respuesta(pregunta, contexto):
    history = get_memory()
    
    prompt = f"""
    Contexto: {contexto}
    Historial: {history}
    Pregunta: {pregunta}
    """

    response = ollama.chat(model='gemma3:4b', messages=[
        {'role': 'user', 'content': prompt},
    ])
    
    respuesta = response['message']['content']
    
    # Esto es vital para que la memoria funcione:
    add_to_memory("Usuario", pregunta)
    add_to_memory("Asistente", respuesta)
    
    return respuesta

