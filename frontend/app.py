import streamlit as st
import requests

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Chat with PDF",
    layout="wide"
)

# ------------------ Session State ------------------
if "pdfs" not in st.session_state:
    st.session_state.pdfs = {}

if "current_pdf" not in st.session_state:
    st.session_state.current_pdf = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------ Sidebar ------------------
st.sidebar.title("📄 PDF Chatbot")

uploaded_pdf = st.sidebar.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_pdf:
    st.session_state.pdfs[uploaded_pdf.name] = uploaded_pdf
    st.session_state.current_pdf = uploaded_pdf.name
    st.sidebar.success(f"Loaded: {uploaded_pdf.name}")

page = st.sidebar.radio(
    "Navigation",
    ["Chat with PDF", "About"]
)

# ------------------ Chat Page ------------------
if page == "Chat with PDF":
    st.title("💬 Chat with your PDF")

    if not st.session_state.current_pdf:
        st.info("Upload a PDF from the sidebar to start chatting.")
    else:
        st.subheader(f"Chatting with: {st.session_state.current_pdf}")

        # Display chat history
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        # Chat input
        user_query = st.chat_input("Ask something about the PDF")

        if user_query:
            # Save user message
            st.session_state.messages.append({
                "role": "user",
                "content": user_query
            })

            with st.chat_message("user"):
                st.write(user_query)

            # Prepare request for Flask
            pdf_file = st.session_state.pdfs[st.session_state.current_pdf]

            files = {
                "pdf": (pdf_file.name, pdf_file.getvalue(), "application/pdf")
            }
            data = {
                "query": user_query
            }

            # Call backend
            with st.spinner("Thinking..."):
                try:
                    response = requests.post(
                        "http://127.0.0.1:5000/chat",
                        files=files,
                        data=data,
                        timeout=120
                    )

                    if response.status_code == 200:
                        answer = response.json().get("answer", "")
                    else:
                        answer = response.json().get("error", "Backend error")

                except Exception as e:
                    answer = f"Error connecting to backend: {e}"

            # Save assistant message
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

            with st.chat_message("assistant"):
                st.write(answer)

# ------------------ About Page ------------------
elif page == "About":
    st.title("About 📚")

    st.markdown(
        """
        This application allows you to chat with your PDF documents using a powerful
        **Retrieval-Augmented Generation (RAG)** system.

        ### 🚀 Features
        - Upload and chat with PDF documents
        - Ask natural language questions
        - Context-aware answers grounded in document content
        - ChatGPT-style conversational interface

        ### 🛠️ Technologies Used
        - **Groq LLM** for fast language generation
        - **FAISS** for vector similarity search
        - **Sentence Transformers** for embeddings
        - **Flask** as backend API
        - **Streamlit** for frontend UI

        ### 📌 How to Use
        1. Upload a PDF using the sidebar
        2. Navigate to **Chat with PDF**
        3. Ask questions related to the document
        4. View answers and chat history in real time

        Enjoy chatting with your PDFs! 📄💬
        """
    )
