from app.rag.retriever import search
from app.llm import generar_respuesta


while True:

    pregunta = input("\nTu pregunta: ")

    context, sources = search(pregunta)

    respuesta = generar_respuesta(pregunta, context)

    print("\nRespuesta:\n")
    print(respuesta)

    print("\nFuentes:")
    for s in sources:
        print("-", s)
        