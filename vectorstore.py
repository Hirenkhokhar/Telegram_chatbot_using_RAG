import os
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

PERSIST_DIRECTORY = "db"
DATA_PATH = "/home/petpooja-108/Documents/projects/Telegram_chatbot_using_RAG/india.txt"

def create_vectorstore():
    loader = TextLoader(DATA_PATH)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=150)
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings()
    vectordb = Chroma.from_documents(documents=texts, embedding=embeddings, persist_directory=PERSIST_DIRECTORY)
    vectordb.persist()

    return vectordb

def load_vectorstore():
    embeddings = HuggingFaceEmbeddings()
    return Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embeddings)