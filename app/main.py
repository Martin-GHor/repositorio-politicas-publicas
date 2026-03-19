from fastapi import FastAPI

app = FastAPI(
    title="Asesor IA en Políticas Públicas",
    description="API académica y técnica para análisis y formulación de políticas públicas",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "mensaje": "Asesor IA de Políticas Públicas funcionando correctamente"
    }
    from fastapi import FastAPI

app = FastAPI(
    title="Asesor IA en Políticas Públicas",
    description="API académica y técnica para análisis y formulación de políticas públicas",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "mensaje": "Asesor IA de Políticas Públicas funcionando correctamente"
    }
    from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Asesor IA en Políticas Públicas",
    description="API académica y técnica para análisis y formulación de políticas públicas",
    version="1.0.0"
)

# Modelo de entrada
class ProblemaPolitica(BaseModel):
    problema: str


@app.get("/")
def read_root():
    return {
        "mensaje": "Asesor IA de Políticas Públicas funcionando correctamente"
    }

from fastapi import FastAPI
from app.api.copiloto import router as copiloto_router

app = FastAPI(title="PolicyLab AI")

app.include_router(copiloto_router)
@app.post("/copiloto-politicas")
def analizar_politica(datos: ProblemaPolitica):

    problema = datos.problema

    return {
        "problema_detectado": problema,

        "diagnostico": "Se identifica una problemática pública que requiere intervención estatal.",

        "actores_clave": [
            "Gobierno municipal",
            "Ciudadanos",
            "Empresas privadas",
            "Organizaciones sociales"
        ],

        "instrumentos_politica": [
            "Regulación",
            "Incentivos económicos",
            "Programas públicos",
            "Infraestructura urbana"
        ],

        "recomendaciones": [
            "Realizar diagnóstico territorial",
            "Incorporar participación ciudadana",
            "Diseñar programa piloto",
            "Establecer indicadores de evaluación"
        ]
    }
    