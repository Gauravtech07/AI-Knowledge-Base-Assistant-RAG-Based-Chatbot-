from llama_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader(
    "data/files"
).load_data()

print("Loaded:", len(documents))

print(documents[0].get_content()[:1000])