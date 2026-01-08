from llama_index.core import VectorStoreIndex,Settings
from llama_index.core.node_parser import SentenceSplitter

from rag.ingestion import load_documents
from config.settings import embed_model,LLM

def build_index(persist_dir: str ="storage"):
    """
    Builds a FAIIS-backend vector index from documents and save it to disk
    
    """

    #register global modals
    Settings.embed_model=embed_model
    Settings.llm=LLM

    #LOAD RAW DOCUMENTS

    documents= load_documents()

    # split documents into chunks
    splitter=SentenceSplitter(
        chunk_size=512,
        chunk_overlap=50
    )

    nodes=splitter.get_nodes_from_documents(documents)

    # build vector index
    index=VectorStoreIndex(nodes)

    ## persist index
    index.storage_context.persist(persist_dir=persist_dir)

    print(f"Index built successfully with {len(nodes)} chunks.")