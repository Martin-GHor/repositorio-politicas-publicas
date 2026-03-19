import streamlit as st

from app.rag.retriever import search
from app.llm import generar_respuesta

st.set_page_config(page_title="Asistente de Políticas Públicas", layout="wide")

st.title("Asistente de Políticas Públicas")
st.write("Análisis inteligente de documentos de política pública")

# selector de modo
modo = st.selectbox(
    "Modo de análisis",
    [
        "Pregunta normal",
        "Comparar políticas",
        "Knowledge Graph"
    ]
)

pregunta = st.text_input("Haz una pregunta sobre políticas públicas")

# ==============================
# MODO PREGUNTA NORMAL
# ==============================

if modo == "Pregunta normal":

    if pregunta:

        context, sources = search(pregunta)

        respuesta = generar_respuesta(pregunta, context)

        st.subheader("Respuesta")
        st.write(respuesta)

        st.subheader("Fuentes")

        for s in sources:
            st.write(
                f"- {s['document']} (página {s['page']})"
            )


# ==============================
# MODO COMPARAR POLÍTICAS
# ==============================

elif modo == "Comparar políticas":

    if pregunta:

        from app.api.compare_policies import compare

        resultado, sources = compare(pregunta)

        st.subheader("Comparación de políticas")

        st.write(resultado)

        st.subheader("Fuentes")

        for s in sources:
            st.write(
                f"- {s['document']} (página {s['page']})"
            )


# ==============================
# MODO KNOWLEDGE GRAPH
# ==============================
elif modo == "Knowledge Graph":

    if pregunta:

        from app.api.knowledge_pipeline import build_knowledge

        relations, graph_file, sources = build_knowledge(pregunta)

        st.subheader("Relaciones detectadas")

        st.write(relations)

        if graph_file:

            st.subheader("Mapa de conocimiento")

            with open(graph_file, "r", encoding="utf-8") as f:
                html = f.read()

            st.components.v1.html(html, height=700)

        else:

            st.warning("No se pudo generar el grafo de conocimiento.")

        st.subheader("Fuentes")

        for s in sources:
            st.write(
                f"- {s['document']} (página {s['page']})"
            )
            


