from llama_index.core import SimpleDirectoryReader
from typing import List

def load_documents(data_dir: str = "data") ->List:
    """
    Load documents from the data directory.
    Supported formats:
    - PDF
    - CSV
    - TXT

    """

    reader = SimpleDirectoryReader(
        input_dir=data_dir,
        recursive=True,
        filename_as_id=True
    )
    documents=reader.load_data()
    return documents



# Scans the data/ folder

# Automatically detects file type

# Converts everything into Document objects

# Adds metadata (filename, path, etc.)