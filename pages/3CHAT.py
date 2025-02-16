import streamlit as st
from transformers import pipeline
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import torch

# 🔑 Token de Hugging Face (Sustituye con tu propio token)
#HF_TOKEN=''
# Cargar modelo de generación de texto con autenticación
# chatbot_pipeline = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B", device=-1)
chatbot_pipeline = pipeline(
    "text-generation", 
    model="meta-llama/Llama-3.2-1B",  # Asegúrate de que el modelo existe en HF
    device=-1,
    # device_map="auto",  # Asigna la GPU automáticamente
    torch_dtype=torch.float16,  # Usa precisión de 16 bits para optimizar memoria
    # use_auth_token=HF_TOKEN  # 🔑 Autenticación con Hugging Face
)

# Cargar base de conocimiento desde un archivo de texto
def cargar_base_conocimiento(archivo="conocimiento_diabetes_limpio.txt"):
    loader = TextLoader(archivo, encoding='utf-8')
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1200, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cuda"}
    )
    vectorstore = FAISS.from_documents(texts, embeddings)
    return vectorstore

# Buscar información relevante en la base de conocimiento
def buscar_informacion(pregunta, vectorstore):
    docs = vectorstore.similarity_search(pregunta, k=2)
    contexto = " ".join([doc.page_content for doc in docs])
    return contexto

# Generar respuesta con contexto
def generar_respuesta(pregunta, contexto):
    prompt = f"""Eres un asistente experto en diabetes. Usa la información del contexto para responder de forma clara y precisa.
Si el contexto no responde directamente a la pregunta, usa tu conocimiento para completarla.

Reglas:
1. No repitas el contexto tal cual.
2. Si el contexto no tiene información suficiente, responde con lo que sabes sobre el tema.
3. Da una respuesta concisa y estructurada.

Pregunta: {pregunta}

Contexto:
{contexto}

Formato de respuesta:
- Explica en términos sencillos.
- Usa frases cortas y directas.
- No repitas el contexto exactamente.

Respuesta:"""

    respuesta = chatbot_pipeline(prompt, max_length=256, truncation=True, temperature=0)[0]["generated_text"]
    return respuesta

# Cargar base de conocimiento
vectorstore = cargar_base_conocimiento()

# Interfaz en Streamlit
st.title("🤖 Chatbot Inteligente sobre Diabetes y el Modelo")

pregunta_usuario = st.text_input("Haz una pregunta:")

if pregunta_usuario:
    contexto = buscar_informacion(pregunta_usuario, vectorstore)
    st.write("🔎 Contexto obtenido:", contexto)
    respuesta = generar_respuesta(pregunta_usuario, contexto)
    st.write("🤖", respuesta)
