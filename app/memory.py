_memory_store = []

def get_memory():
    global _memory_store
    if not _memory_store:
        return "No hay historial previo."
    return "\n".join([f"{m['role']}: {m['content']}" for m in _memory_store])

def add_to_memory(role, content):
    global _memory_store
    _memory_store.append({"role": role, "content": content})
    if len(_memory_store) > 10:
        _memory_store.pop(0)
