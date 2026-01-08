from llama_index.core import (
    StorageContext,
    load_index_from_storage,
    Settings,
)

from config.settings import embed_model, LLM


def query_rag(question: str, persist_dir: str = "storage"):
    """
    Query the RAG system using FAISS + HuggingFace embeddings + Ollama LLM.
    """

    # MUST be set BEFORE loading index
    Settings.embed_model = embed_model
    Settings.llm = LLM

    # Load stored index
    storage_context = StorageContext.from_defaults(
        persist_dir=persist_dir
    )

    index = load_index_from_storage(storage_context)

    # Create query engine
    query_engine = index.as_query_engine(
        similarity_top_k=5
    )

    response = query_engine.query(question)
    return response
