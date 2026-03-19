def compare_policies(question):
    print("DEBUG: Iniciando función...")
    try:
        context, sources = search(question)
        print(f"DEBUG: Search funcionó. Contexto: {len(str(context))} caracteres.")

        prompt = f"Compara: {context}\nPregunta: {question}"

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False},
            timeout=15
        )
        
        # Si la respuesta no es 200, esto lanza una excepción y va al except
        response.raise_for_status() 
        
        result = response.json()
        respuesta = result.get("response", "Sin respuesta")
        
        print("DEBUG: Llegando al return con éxito.")
        return respuesta, sources

    except Exception as e:
        print(f"DEBUG: ERROR capturado: {e}")
        return f"Error: {str(e)}", []

# PRUEBA DIRECTA
print(compare_policies("test"))
