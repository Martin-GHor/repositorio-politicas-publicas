from app.rag.retriever import search

def compare(question: str):

    context, sources = search(question)

    resultado = f"""
Análisis comparativo de políticas públicas

Pregunta:
{question}

Información encontrada:

{context[:1200]}
"""

    return resultado, sources
 


    

