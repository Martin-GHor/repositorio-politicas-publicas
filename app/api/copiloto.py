from fastapi import APIRouter
from app.rag.retriever import search

router = APIRouter()

@router.get("/copiloto")

def preguntar(q: str):

    resultados = search(q)

    return {
        "pregunta": q,
        "resultados": resultados
    }