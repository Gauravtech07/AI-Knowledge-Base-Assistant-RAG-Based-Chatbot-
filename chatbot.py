import os
from dotenv import load_dotenv

load_dotenv()

from llama_index.core import VectorStoreIndex
from llama_index.core import SimpleDirectoryReader

from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding

def create_chat_engine():

    documents = SimpleDirectoryReader(
        "data/files"
    ).load_data()

    llm = Gemini(
         model="models/gemini-2.5-flash",
        api_key=os.getenv("GOOGLE_API_KEY")
    )

    embed_model = GeminiEmbedding(
        model_name="models/gemini-embedding-001",
        api_key=os.getenv("GOOGLE_API_KEY")
    )

    index = VectorStoreIndex.from_documents(
        documents,
        embed_model=embed_model
    )

    chat_engine = index.as_chat_engine(
        llm=llm,
        chat_mode="context"
    )

    return chat_engine