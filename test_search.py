from app.rag.retriever import search
from app.llm import generar_respuesta

pregunta = "¿Qué es el ciclo de políticas públicas?"

print("Pregunta:", pregunta)
print()

# Buscar documentos relevantes
resultados = search(pregunta)

# Mostrar resultados encontrados
for i, r in enumerate(resultados):
    print("Resultado", i + 1)
    print(r)
    print()

# Construir contexto para el modelo
contexto = "\n".join(resultados)

# Generar respuesta con el modelo
respuesta = generar_respuesta(pregunta, contexto)

print("\nRESPUESTA DEL SISTEMA:\n")
print(respuesta)