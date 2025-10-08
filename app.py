import streamlit as st
import os
import faiss
from dotenv import load_dotenv, set_key
from langchain_community.document_loaders import PyPDFLoader
from RAG_01_Dataloader.data_loader_and_spilitter import split_text
from RAG_02_vector_Embedding.embedding_and_vector_DB_store import create_vector_DB, chunks_map
from RAG_03_Augument_and_Generation.Retreiver_and_prompt_generation import retrieve_top_k, build_prompt
from utils.utils import generate_completion

# ---------------- Streamlit Page Config ----------------
st.set_page_config(
    page_title="📘 LangChain PDF Chatbot",
    page_icon="💬",
    layout="wide"
)

st.title("💬 LangChain PDF Chatbot")
st.caption("Upload a PDF and chat with its contents using RAG (Retrieval-Augmented Generation)")

# ---------------- Sidebar Configuration ----------------
with st.sidebar:
    st.header("⚙️ Settings")
    st.markdown("""
    1. Enter your **Euron / OpenAI API key**  
    2. Upload your PDF  
    3. The system will check if a FAISS index exists  
    4. Ask questions about the content  
    5. Type **exit** to end the chat and clean up
    """)

# ---------------- Load or Create .env ----------------
dotenv_path = ".env"
if not os.path.exists(dotenv_path):
    with open(dotenv_path, "w") as f:
        f.write("")  # create empty .env if not exists

load_dotenv(dotenv_path)

# ---------------- API Key Management ----------------
st.subheader("🔐 Enter Your API Key")

# Load existing key (if available)
saved_key = os.getenv("euri_api_key", "")

if "api_key" not in st.session_state:
    st.session_state.api_key = saved_key

api_key_input = st.text_input(
    "Enter your Euron or OpenAI-compatible API key:",
    type="password",
    placeholder="sk-xxxxxxxxxxxxxxxxxxxxxxxx",
    value=st.session_state.api_key
)

# Save the key to .env when entered
if api_key_input:
    st.session_state.api_key = api_key_input.strip()
    set_key(dotenv_path, "euri_api_key", st.session_state.api_key)
    os.environ["euri_api_key"] = st.session_state.api_key
    st.success("✅ API key stored in .env and set successfully!")
else:
    st.warning("⚠️ Please enter your API key to continue.")
    st.stop()  # Stop app execution until key is provided

# ---------------- Session State ----------------
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None
if "chunk_map" not in st.session_state:
    st.session_state.chunk_map = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- File Upload ----------------
uploaded_file = st.file_uploader("📂 Upload your PDF file", type=["pdf"])

if uploaded_file:
    # Save temporarily
    os.makedirs("Artifacts", exist_ok=True)
    with open("Artifacts/temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info("📄 Loading PDF...")
    loader = PyPDFLoader("Artifacts/temp.pdf")
    documents = loader.load()
    st.success(f"✅ Loaded {len(documents)} pages from the PDF!")

    chunks = split_text(documents)

    # --- Check if FAISS index exists ---
    os.makedirs("vector_database", exist_ok=True)
    index_path = "vector_database/index.faiss"

    if os.path.exists(index_path):
        st.success("📁 Found existing FAISS index. Loading it...")
        vector_db = faiss.read_index(index_path)
        chunk_map = chunks_map(chunks)
    else:
        with st.spinner("⚙️ Creating FAISS vector database..."):
            vector_db, chunk_map = create_vector_DB(chunks)
            # faiss.write_index(vector_db, index_path)
        st.success("✅ Vector database created and saved!")

    st.session_state.vector_db = vector_db
    st.session_state.chunk_map = chunk_map

    st.write("📏 Length of chunk map:", len(chunk_map))

# ---------------- Chat Interface ----------------
if st.session_state.vector_db is not None:
    st.divider()
    st.subheader("💬 Chat with your PDF")

    # Display previous messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input for user query
    if prompt := st.chat_input("Ask a question (type 'exit' to end chat)..."):
        if prompt.lower().strip() == "exit":
            st.info("👋 Chat ended. Thank you!")

            # --- Delete FAISS index file ---
            index_path = "vector_database/index.faiss"
            if os.path.exists(index_path):
                try:
                    os.remove(index_path)
                    st.success("🧹 FAISS index deleted successfully!")
                except Exception as e:
                    st.error(f"⚠️ Error deleting index file: {e}")

            # --- Delete temporary PDF ---
            if os.path.exists("Artifacts/temp.pdf"):
                try:
                    os.remove("Artifacts/temp.pdf")
                    st.success("🧾 Temporary PDF removed!")
                except Exception as e:
                    st.error(f"⚠️ Error deleting temp PDF: {e}")

            st.stop()

        # Display user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # --- Retrieve and generate response ---
        with st.chat_message("assistant"):
            with st.spinner("🔍 Searching for relevant information..."):
                top_k = retrieve_top_k(prompt, st.session_state.vector_db, st.session_state.chunk_map)
                query_prompt = build_prompt(top_k, prompt)
                response = generate_completion(query_prompt)

            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

else:
    st.warning("📄 Please upload a PDF to start chatting.")