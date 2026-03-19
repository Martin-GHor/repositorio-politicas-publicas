import streamlit as st
import requests
import os

from app.rag.retriever import search
from app.api.compare_policies import compare_policies

st.set_page_config(
    page_title="Policy Intelligence Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Policy Intelligence Assistant")
st.write("Sistema de análisis de políticas públicas con IA")

# -----------------------------
# SUBIR NUEVOS DOCUMENTOS
# -----------------------------

st.sidebar.header("📂 Agregar documentos")

uploaded_file = st.sidebar.file_uploader(
    "Subir nuevo PDF",
    type=["pdf"]
)

if uploaded_file:

    save_path = os.path.join("knowledge", uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.sidebar.success(f"Documento guardado: {uploaded_file.name}")

    if st.sidebar.button("Reindexar documentos"):

        os.system("python build_index.py")

        st.sidebar.success("Índice actualizado")

# -----------------------------
# MODO DE ANÁLISIS
# -----------------------------

modo = st.selectbox(
    "Modo de análisis",
    [
        "Pregunta normal",
        "Comparar políticas"
    ]
)

pregunta = st.text_input(
    "Haz una pregunta sobre los documentos:"
)

# -----------------------------
# PROCESAR PREGUNTA
# -----------------------------

if pregunta:

    with st.spinner("Analizando documentos..."):

        if modo == "Pregunta normal":

            context, sources = search(pregunta)

            prompt = f"""
Eres un experto en políticas públicas.

Usa SOLO la información del contexto.

Contexto:
{context}

Pregunta:
{pregunta}

Respuesta clara y bien estructurada:
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
            respuesta = result["response"]

        else:

            respuesta, sources = compare_policies(pregunta)

        # -----------------------------
        # MOSTRAR RESPUESTA
        # -----------------------------

        st.subheader("📌 Respuesta")
        st.write(respuesta)

        # -----------------------------
        # MOSTRAR FUENTES
        # -----------------------------

        st.subheader("📚 Fuentes")

        for i, source in enumerate(sources):

            with st.expander(f"Fuente {i+1}"):

                st.write(f"📄 Documento: {source['document']}")
                st.write(f"📑 Página: {source['page']}")

                st.write("Fragmento relevante:")

                st.info(source["snippet"])
                







        
