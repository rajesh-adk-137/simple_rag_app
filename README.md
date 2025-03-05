

# RAG PDF Chat Assistant

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-FF4B4B.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A Retrieval-Augmented Generation (RAG) based application that allows users to upload PDF documents and ask questions about their content. The system uses state-of-the-art NLP models to provide accurate answers by combining information retrieval and text generation.

## Features

- **PDF Upload**: Upload any PDF document
- **Interactive Chat**: Ask questions about the document content
- **RAG Architecture**: Combines retrieval and generation for accurate answers
- **User-friendly Interface**: Built with Streamlit for easy interaction
- **Efficient Processing**: Uses FAISS for fast similarity search

## Technology Stack

- **Backend**: Python
- **NLP Models**: 
  - Sentence Transformers (all-MiniLM-L6-v2) for embeddings
  - T5 (Text-to-Text Transfer Transformer) for answer generation
- **Vector Search**: FAISS (Facebook AI Similarity Search)
- **Web Interface**: Streamlit

## Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

1. Clone the repository:
   ```bash
   https://github.com/rajesh-adk-137/simple_rag_app.git
   cd simple_rag_app
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv rag-env
   # Windows
   rag-env\Scripts\activate
   # Linux/Mac
   source rag-env/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download NLP models. This will happen automatically on first run.(The installtion may take time.)

### Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## Usage

1. Open the application in your browser
2. Upload a PDF document
3. Wait for the document to process (this may take a few moments)
4. Enter your question in the text box
5. View the generated answer

## Project Structure

```
simple_rag_app/
├── app.py                # Main Streamlit application
├── rag_model.py          # RAG model implementation
├── pdf_processor.py      # PDF processing 
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Files to ignore in version control
```

## Configuration

The application uses default settings, but you can configure:

- Chunk size for text splitting (in `pdf_processor.py`)
- Number of retrieved chunks (in `rag_model.py`)
- Model parameters (in `rag_model.py`)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- Hugging Face for the Transformers library
- Facebook AI Research for FAISS
- Streamlit for the web framework
- Sentence Transformers for embedding models

---


## Screenshots

![Example-query-1](https://github.com/user-attachments/assets/dfba8e69-95ad-4032-9cf1-6571ebfe250e)

![Example-query-2](https://github.com/user-attachments/assets/a9793f21-facb-497c-acf5-dfec3c3f8f24)

---


## Roadmap

- [✅ ] Basic PDF processing
- [✅ ] RAG implementation
- [✅ ] Streamlit interface
- [x] Add support for multiple file formats
- [x] Implement document summarization
- [x] Add user authentication
- [x] Create API endpoint for integration
