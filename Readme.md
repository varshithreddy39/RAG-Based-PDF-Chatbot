# 🤖 RAG-Based PDF Chatbot

A full-stack Retrieval-Augmented Generation (RAG) system to chat with PDF documents

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FE6F61?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![FAISS](https://img.shields.io/badge/FAISS-FF6B35?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAiIGhlaWdodD0iNDAiIHZpZXdCb3g9IjAgMCA0MCA0MCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMjAiIGN5PSIyMCIgcj0iMjAiIGZpbGw9IiNGRjZCMzUiLz4KPC9zdmc+Cg==)](https://faiss.ai/)

An end-to-end GenAI application that allows users to upload PDF documents and ask natural-language questions about their content. The system uses Retrieval-Augmented Generation (RAG) with FAISS vector search and LLM-based answering, exposed via a Flask API and consumed through a Streamlit chat interface.

## ✨ Key Features

- 📄 Upload and chat with PDF documents
- 🧠 Retrieval-Augmented Generation (RAG) pipeline
- 🔍 Semantic search using FAISS
- ❌ Hallucination control (answers only from document context)
- 💬 ChatGPT-style conversational UI
- 🧱 Clean modular codebase
- ⚡ Fast LLM inference using Groq

## 🏗️ System Architecture

User
↓
Streamlit Frontend (UI)
↓ HTTP POST (PDF + Query)
Flask Backend (API)
↓
RAG Pipeline
├── PDF Text Extraction
├── Text Cleaning
├── Chunking
├── Embedding Generation
├── FAISS Vector Search
├── Context Construction
├── Prompt Engineering
└── LLM Answer Generation

text

## 📁 Project Structure

RAG/
├── backend/
│ ├── init.py
│ └── app.py # Flask backend API
│
├── core/
│ ├── build_context.py # Context construction
│ ├── chunk_text.py # Text chunking logic
│ ├── clean_text.py # Text cleaning
│ ├── embeddings.py # Embedding generation
│ ├── extract_text.py # PDF text extraction
│ ├── llm.py # Groq LLM interface
│ ├── prompt.py # Prompt construction
│ └── vectordb.py # FAISS vector database
│
├── frontend/
│ └── streamlit_app.py # Streamlit chat UI
│
├── rag_pipeline.py # Orchestrates full RAG flow
├── requirements.txt
├── .env # Environment variables
└── README.md

text

## 🛠️ Technology Stack

### Backend
- **Python** - Core language
- **Flask** – REST API layer
- **FAISS** – Vector similarity search
- **Sentence-Transformers** – Text embeddings
- **Groq LLM** – Language model inference
- **PyPDF2** – PDF text extraction

### Frontend
- **Streamlit** – Interactive chat interface

## ⚙️ How the RAG Pipeline Works

1. **PDF Upload** - User uploads a PDF through the Streamlit UI
2. **Text Extraction & Cleaning** - Raw text is extracted and normalized
3. **Chunking** - Text is split into overlapping chunks for better retrieval
4. **Embedding Generation** - Each chunk is converted into a dense vector
5. **Vector Search (FAISS)** - Query embedding is matched with top-K relevant chunks
6. **Context Construction** - Retrieved chunks are combined into a single context
7. **Prompt Engineering** - A controlled prompt ensures document-grounded answers
8. **LLM Answer Generation** - Groq LLM generates the final response

## ▶️ How to Run the Application

### 1️⃣ Create Virtual Environment
```bash
python -m venv myenv
source myenv/bin/activate   # macOS/Linux
myenv\Scripts\activate      # Windows
2️⃣ Install Dependencies
bash
pip install -r requirements.txt
3️⃣ Set Environment Variable
bash
export GROQ_API_KEY="your_api_key_here"   # macOS/Linux
setx GROQ_API_KEY "your_api_key_here"     # Windows
4️⃣ Run Flask Backend
bash
cd RAG
python backend/app.py
Backend runs at: http://127.0.0.1:5000

5️⃣ Run Streamlit Frontend
bash
cd RAG
streamlit run frontend/streamlit_app.py
Frontend opens at: http://localhost:8501

🧪 Example Questions
What is the project about?

Explain the milestones.

What technologies are used?

What problem does this system solve?

🔒 Hallucination Control
Answers are generated only from retrieved document context. If the information is missing, the system responds with:

Not found in the document.

This ensures trustworthy and reliable answers.

🎯 Use Cases
Research paper analysis

Academic document summarization

Technical documentation Q&A

Knowledge-base search systems

📌 Future Enhancements
📎 Source citations with chunk references

⚡ Vector DB caching per PDF

🐳 Dockerization

🌐 Cloud deployment

👥 Multi-user support

🧠 Interview Highlight
Designed and implemented a modular RAG system using FAISS and LLMs, deployed via a Flask API and Streamlit UI with strict hallucination control.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

⭐ Show Your Support
If you found this project useful, please give it a ⭐ on GitHub!

🚀 Built with ❤️ for intelligent document understanding
Made by Varshith Reddy