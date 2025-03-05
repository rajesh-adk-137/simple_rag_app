import PyPDF2
import numpy as np
from typing import List

def read_pdf(file_path: str) -> str:
    """Extract text from PDF file"""
    text = ""
    with open(file_path, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def split_text(text: str, max_length: int = 500) -> List[str]:
    """Split text into chunks"""
    lines = text.split('\n')
    chunks = []
    current_chunk = ""
    
    for line in lines:
        if not line.strip():
            continue
        if len(current_chunk) + len(line) > max_length:
            chunks.append(current_chunk.strip())
            current_chunk = line + " "
        else:
            current_chunk += line + " "
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks