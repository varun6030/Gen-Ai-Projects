from rag.ingestion import load_documents

docs=load_documents()
print(f"Number of documents loaded {len(docs)}")
print("First document preview : ")
print(docs[0])