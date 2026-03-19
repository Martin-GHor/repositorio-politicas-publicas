from app.rag.retriever import search
from app.analysis.knowledge_graph import extract_relations
from app.analysis.graph_visualizer import crear_mapa


def build_knowledge(question):

    # buscar información en los documentos
    context, sources = search(question)

    # extraer relaciones del texto
    relations = extract_relations(context)

    # crear mapa visual
    graph_file = crear_mapa(relations)

    return relations, graph_file, sources

    