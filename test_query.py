from rag.query_engine import query_rag

question="what is this document about?"
response=query_rag(question)

print("Answer")
print(response)

print("\nSources:")

for node in response.source_nodes:
    print(node.metadata)