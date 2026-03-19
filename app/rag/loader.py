
import os
from langchain_community.document_loaders import PyPDFLoader, CSVLoader

KNOWLEDGE_PATH = "knowledge"

def load_all_knowledge():

    documents = []

    for file in os.listdir(KNOWLEDGE_PATH):

        path = os.path.join(KNOWLEDGE_PATH, file)

        # PDFs
        if file.endswith(".pdf"):

            if os.path.getsize(path) < 100:
                print("PDF ignorado (archivo vacío o corrupto):", file)
                continue

            loader = PyPDFLoader(path)
            docs = loader.load()
            documents.extend(docs)

        # CSV
        elif file.endswith(".csv"):

            loader = CSVLoader(file_path=path)
            docs = loader.load()
            documents.extend(docs)

    return documents
    