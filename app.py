import streamlit as st
import os
import faiss
from langchain_community.document_loaders import PyPDFLoader
from RAG_01_Dataloader.data_loader_and_spilitter import split_text
from RAG_02_vector_Embedding.embedding_and_vector_DB_store import create_vector_DB,chunks_map
from RAG_03_Augument_and_Generation.Retreiver_and_prompt_generation import retrieve_top_k, build_prompt
from utils.utils import generate_completion

# Streamlit Page Config
st.set_page_config(
    page_title="📘 LangChain PDF Chatbot",
    page_icon="💬",
    layout="wide"
)

st.title("💬 LangChain PDF Chatbot")
st.caption("Upload a PDF and chat with its contents using RAG (Retrieval-Augmented Generation)")

# --- Sidebar for Configuration ---
with st.sidebar:
    st.header("⚙️ Settings")
    st.markdown("""
    1. Upload your PDF  
    2. The system will check if a FAISS index exists.  
    3. Ask questions about the content!  
    4. Type **exit** to end the chat.
    """)

# --- Session State ---
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None
if "chunk_map" not in st.session_state:
    st.session_state.chunk_map = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- File Upload ---
uploaded_file = st.file_uploader("📂 Upload your PDF file", type=["pdf"])

if uploaded_file:
    # Save temporarily
    with open("Artifacts/temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info("📄 Loading PDF...")
    loader = PyPDFLoader("Artifacts/temp.pdf")
    documents = loader.load()
    st.success(f"✅ Loaded {len(documents)} pages from the PDF!")

    chunks = split_text(documents)

    # --- Check if FAISS index exists ---
    index_path = "vector_database/index.faiss"
    os.makedirs("vector_database", exist_ok=True)

    if os.path.exists(index_path):
        st.success("📁 Found existing FAISS index. Loading it...")
        vector_db = faiss.read_index(index_path)
        # load corresponding chunk map (ensure you save it when creating DB)
        chunk_map = chunks_map(chunks)  # Assuming chunks_map function returns the mapping
    else:
        with st.spinner("⚙️ Creating FAISS vector database..."):
            vector_db, chunk_map = create_vector_DB(chunks)
            faiss.write_index(vector_db, index_path)
        st.success("✅ Vector database created and saved!")

    st.session_state.vector_db = vector_db
    st.session_state.chunk_map = chunk_map

    st.write("The lenght of the chunk map is ",len(chunk_map))

# --- Chat Interface ---
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

            # Also remove temporary PDF
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

