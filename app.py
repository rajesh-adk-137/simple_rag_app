import streamlit as st
import tempfile
import os
from pdf_processor import read_pdf, split_text
from rag_model import RAGSystem

def main():
    st.title("PDF Chat Assistant")
    st.write("Upload a PDF and ask questions about its content")
    
    # Initialize RAG system
    if "rag" not in st.session_state:
        st.session_state.rag = RAGSystem()
    
    # File upload
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    
    if uploaded_file is not None:
        # Save uploaded file to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name
        
        # Process PDF
        with st.spinner("Processing PDF..."):
            text = read_pdf(tmp_path)
            chunks = split_text(text)
            st.session_state.rag.build_index(chunks)
        
        os.unlink(tmp_path)  # Clean up temp file
    
    # Question input
    question = st.text_input("Enter your question:")
    
    if question and "rag" in st.session_state:
        with st.spinner("Searching for answer..."):
            try:
                answer = st.session_state.rag.answer_query(question)
                st.subheader("Answer:")
                st.write(answer)
            except Exception as e:
                st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()