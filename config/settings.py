from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

#embedding model

embed_model =HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

## local LLM via Ollama

LLM=Ollama(
    model="mistral",
    temperature=0.1,
    request_timeout=120
)