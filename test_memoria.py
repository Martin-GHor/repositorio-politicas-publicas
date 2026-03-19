from app.memory import get_memory, add_to_memory

print("--- TEST DE MEMORIA ---")
add_to_memory("Usuario", "Prueba de politica publica")
print("Contenido guardado:")
print(get_memory())
