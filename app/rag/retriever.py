from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# modelo de embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# cargar vectorstore
vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

# retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)


def search(query: str):

    docs = retriever.invoke(query)

    context_parts = []
    sources = []

    for doc in docs:

        metadata = doc.metadata if doc.metadata else {}

        snippet = doc.page_content.strip()

        context_parts.append(snippet)

        sources.append({
            "document": metadata.get("source", "Documento desconocido"),
            "page": metadata.get("page", "N/A"),
            "snippet": snippet[:350]
        })

    context = "\n\n".join(context_parts)

    return context, sources
    
    
    

            
    




    
