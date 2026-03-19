import ollama

response = ollama.chat(
    model="mistral",
    messages=[
        {"role": "user", "content": "Explica brevemente qué es una política pública"}
    ]
)

print(response["message"]["content"])