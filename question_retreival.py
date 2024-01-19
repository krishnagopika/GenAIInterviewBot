
# Optional code for storing and retreiving questions from Vectro DB
from langchain.embeddings import HuggingFaceEmbeddings
import chromadb

embeddings = HuggingFaceEmbeddings(
    model_name="thenlper/gte-large",
    encode_kwargs={"normalize_embeddings": True},
)
from langchain.vectorstores import Chroma
chroma_client = chromadb(host='3.81.96.18', port=8000)
chromadb.PersistentClient()
vectordb = Chroma.from_documents(documents=texts, embedding=embeddings, client=chroma_client)