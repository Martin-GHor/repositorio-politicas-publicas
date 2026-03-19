from app.rag.loader import load_all_knowledge

print("Cargando conocimiento...")

docs = load_all_knowledge()

print("Documentos cargados:", len(docs))