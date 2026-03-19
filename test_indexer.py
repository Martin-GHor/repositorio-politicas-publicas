from app.rag.indexer import build_index

print("Construyendo índice...")

index, docs = build_index()

print("Index listo")
