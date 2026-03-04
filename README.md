
# 📄 PDF Chat RAG Application

A **Retrieval-Augmented Generation (RAG)** based application that allows users to upload PDF documents and interact with them through a conversational AI chatbot.

This project extracts text from PDFs, converts it into embeddings, stores it in a vector database, and retrieves relevant content to generate accurate answers using an LLM.

---

## 🚀 Features

* 📂 Upload PDF documents
* ✂️ Automatic text chunking
* 🔎 Semantic search using vector embeddings
* 🧠 Context-aware response generation
* 💬 Interactive chat interface (Streamlit)
* 🗂 Modular RAG pipeline structure

---

## 🏗️ Project Architecture

The project follows a modular RAG pipeline:

1. **Data Loader**

   * Extracts text from PDF
   * Cleans and prepares text

2. **Text Splitting**

   * Splits document into smaller chunks

3. **Embedding Generation**

   * Converts text chunks into vector embeddings

4. **Vector Database**

   * Stores embeddings for fast similarity search

5. **Retriever**

   * Retrieves relevant chunks based on user query

6. **Generator (LLM)**

   * Generates final answer using retrieved context

---

## 📁 Project Structure

```
Pdf_Chat_RAG_Application/
│
├── app.py                          # Main Streamlit application
├── requirements.txt                # Dependencies
├── README.md                       # Project documentation
│
├── Langchain_Application/          # LangChain-based RAG implementation
├── Langgraph_Application/          # LangGraph-based workflow
│
├── RAG_01_Dataloader/              # PDF loading logic
├── RAG_02_vector_Embedding/        # Embedding creation
├── RAG_03_Augument_and_Generation/ # Retrieval + LLM response
│
├── vector_database/                # Stored vector embeddings
└── utils/                          # Helper functions
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/shreyasmendhekar77/Pdf_Chat_RAG_Application.git
cd Pdf_Chat_RAG_Application
```

### 2️⃣ Create virtual environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

If your project uses OpenAI or any other LLM API, create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

Or export manually:

**Mac/Linux**

```bash
export OPENAI_API_KEY=your_api_key_here
```

**Windows PowerShell**

```powershell
setx OPENAI_API_KEY "your_api_key_here"
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`).

---

## 🧪 How It Works

1. User uploads a PDF
2. Text is extracted and split into chunks
3. Chunks are converted into embeddings
4. Embeddings are stored in a vector database
5. User asks a question
6. System retrieves relevant chunks
7. LLM generates contextual answer

---

## 🛠 Technologies Used

* Python
* Streamlit
* LangChain / LangGraph
* Vector Database (FAISS or similar)
* OpenAI / LLM API

---

## 📌 Future Improvements

* Multi-PDF support
* Persistent vector storage
* Chat history memory
* Authentication system
* Deployment on cloud (Streamlit Cloud / Render / AWS)
* Docker support

---

## 🎯 Use Cases

* Research paper Q&A
* Academic study assistant
* Legal document analysis
* Business report analysis
* Personal knowledge assistant

---

## 🤝 Contributing

Feel free to fork this repository and submit pull requests.

---

## 📜 License

This project is open-source and available under the MIT License.

---
