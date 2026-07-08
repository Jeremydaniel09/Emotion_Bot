import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbedding

class llm():
    def __init__(self):
        load_dotenv()

        GROQ_API_KEY = os.getenv("GROQ_API_KEY")

        self.chatbot = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.5)

        embedding_function = HuggingFaceEmbedding("")

        self.chroma_db = Chroma(persist_directory="./chroma_db",
                                embedding_function=embedding_function)
        
    def chat(self, message):
        pass