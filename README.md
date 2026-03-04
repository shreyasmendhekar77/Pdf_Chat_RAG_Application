📄 PDF Chat RAG ApplicationAn end-to-end Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and engage in context-aware conversations with their data.This project leverages semantic search to bridge the gap between static documents and LLM intelligence, ensuring accurate, evidence-based answers.🚀 FeaturesPDF Processing: Seamlessly upload and extract text from complex PDF layouts.Intelligent Chunking: Automatic text splitting to maintain semantic coherence.Semantic Search: Uses high-dimensional vector embeddings for precise information retrieval.Dual Implementations: Includes both standard LangChain and agentic LangGraph workflows.Interactive UI: A clean, responsive chat interface built with Streamlit.Modular Design: Separated logic for data loading, embedding, and generation for easy scaling.🏗️ Project ArchitectureThe application follows a modular pipeline to transform raw PDF data into actionable insights:StageProcessDescription1. Data LoaderExtractionReads PDF content and cleans noise/metadata.2. Text SplittingChunkingBreaks text into manageable pieces for the LLM.3. EmbeddingVectorizationConverts chunks into numerical vectors using OpenAI/HuggingFace models.4. Vector DBStorageStores vectors (e.g., FAISS/ChromaDB) for fast similarity search.5. RetrieverSearchFinds the top-$k$ most relevant chunks based on a user's query.6. GeneratorLLM SynthesisPass context + query to the LLM to generate the final response.📁 Project StructureBashPdf_Chat_RAG_Application/
│
├── app.py                          # Main Streamlit UI entry point
├── requirements.txt                # Python dependencies
├── README.md                       # Documentation
│
├── Langchain_Application/          # Sequential RAG implementation
├── Langgraph_Application/          # Cyclic/Agentic RAG workflow
│
├── RAG_01_Dataloader/              # Logic for PDF parsing
├── RAG_02_vector_Embedding/        # Embedding generation & DB logic
├── RAG_03_Augument_and_Generation/ # Prompt engineering & LLM calls
│
├── vector_database/                # Local persistent vector storage
└── utils/                          # Common helper functions
⚙️ Installation & Setup1. Clone the repositoryBashgit clone https://github.com/shreyasmendhekar77/Pdf_Chat_RAG_Application.git
cd Pdf_Chat_RAG_Application
2. Create a Virtual EnvironmentWindows:Bashpython -m venv venv
venv\Scripts\activate
Mac/Linux:Bashpython3 -m venv venv
source venv/bin/activate
3. Install DependenciesBashpip install -r requirements.txt
4. Environment VariablesCreate a .env file in the root directory and add your API keys:Code snippetOPENAI_API_KEY=your_openai_api_key_here
▶️ Running the ApplicationLaunch the Streamlit dashboard with the following command:Bashstreamlit run app.py
Once running, access the local server at http://localhost:8501.🛠 Technologies UsedLanguage: Python 3.9+Orchestration: LangChain & LangGraphFrontend: StreamlitVector Store: FAISS / ChromaDBLLMs: OpenAI GPT-4o / Claude / Local LLMs (via Ollama)Embeddings: OpenAI text-embedding-3-small📌 Future Roadmap[ ] Support for multi-PDF uploads and cross-document querying.[ ] Integration with Pinecone or Weaviate for cloud-scale storage.[ ] Persistent chat history (memory) across sessions.[ ] Support for scanned PDFs via OCR (Tesseract/PaddleOCR).[ ] Containerization with Docker.📜 LicenseDistributed under the MIT License. See LICENSE for more information.
