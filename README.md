# 💬 LangChain PDF Chatbot (RAG Application)

### 📘 Chat with Your PDF Using Retrieval-Augmented Generation (RAG)

This Streamlit-based application enables you to **upload a PDF and interact with its contents conversationally** using **Retrieval-Augmented Generation (RAG)**.  
It combines **LangChain**, **FAISS**, and **LLM APIs (like OpenAI)** to deliver contextually accurate responses grounded in your document.

---

## 🚀 Features

✅ **PDF Upload & Parsing** — Load and extract text from multi-page PDF files.  
✅ **Text Chunking** — Splits the content into optimized text chunks for semantic retrieval.  
✅ **Vector Embedding with FAISS** — Stores document embeddings in a FAISS vector database for efficient similarity search.  
✅ **Contextual Q&A** — Retrieve the most relevant document chunks and generate answers using a Large Language Model.  
✅ **Interactive Chat Interface** — Streamlit-powered chat UI for real-time interaction.  
✅ **Auto Cleanup** — Automatically removes temporary PDF and FAISS index when you end the chat session.  

---

## 🧩 Project Structure

📂 LangChain_PDF_Chatbot
│
├── 📄 app.py # Main Streamlit application
│
├── 📂 RAG_01_Dataloader/
│ └── data_loader_and_spilitter.py # Loads and splits PDF into chunks
│
├── 📂 RAG_02_vector_Embedding/
│ └── embedding_and_vector_DB_store.py # Handles embedding creation and FAISS index storage
│
├── 📂 RAG_03_Augument_and_Generation/
│ └── Retreiver_and_prompt_generation.py # Retrieves top chunks and builds prompt
│
├── 📂 utils/
│ └── utils.py # LLM generation and utility functions
│
├── 📂 vector_database/
│ └── index.faiss # FAISS index file (auto-generated)
│
├── 📂 Artifacts/
│ └── temp.pdf # Temporary uploaded PDF
│
├── 📄 requirements.txt # Project dependencies
└── 📄 README.md # Documentation



---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/LangChain-PDF-Chatbot.git
cd LangChain-PDF-Chatbot

python -m venv venv
# Activate
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows

pip install -r requirements.txt

💻 Running the Application

Start the app using:

streamlit run app.py


Once launched, open the local URL displayed (default: http://localhost:8501
).

🧠 How It Works (RAG Pipeline Overview)
🔹 Step 1: PDF Upload

You upload a .pdf file using Streamlit’s file uploader.

The file is temporarily saved as Artifacts/temp.pdf.

🔹 Step 2: PDF Loading & Splitting

The document is parsed using PyPDFLoader from langchain_community.document_loaders.

split_text() divides the PDF text into manageable chunks.

🔹 Step 3: Vector Embedding & Storage

Each chunk is converted into an embedding vector.

A FAISS index (index.faiss) stores these embeddings for similarity-based retrieval.

🔹 Step 4: Query & Retrieval

When you enter a question, retrieve_top_k() fetches the most semantically relevant text chunks.

🔹 Step 5: Prompt Construction

build_prompt() creates a context-aware prompt containing retrieved text and your question.

🔹 Step 6: Answer Generation

generate_completion() sends the prompt to an LLM (e.g., GPT) to generate the final answer.

🔹 Step 7: Auto Cleanup

Typing exit in the chat:

Deletes the FAISS index (index.faiss)

Removes temporary PDF file (temp.pdf)

Ends the session gracefully

💬 Chat Interface

Chat messages are displayed interactively:

User Message → Blue bubble

Assistant Response → Gray/white bubble

Supports continuous multi-turn conversation.

Type exit anytime to stop the chat and clean up resources.

📘 LangChain PDF Chatbot
----------------------------------
📂 Upload your PDF file
✅ Loaded 12 pages from PDF
⚙️ Creating FAISS vector database...
✅ Vector DB created and saved!

💬 Ask a question (type 'exit' to end chat)
> What is the summary of chapter 3?

🔍 Searching for relevant information...
Answer: Chapter 3 primarily discusses the implementation of the model architecture...
