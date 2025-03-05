import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class RAGSystem:
    def __init__(self):
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.tokenizer = AutoTokenizer.from_pretrained("t5-base")
        self.gen_model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
        self.faiss_index = None
        self.chunks = []
    
    def build_index(self, chunks: list):
        """Build FAISS index from text chunks"""
        chunk_embeddings = self.embedder.encode(chunks)
        dimension = chunk_embeddings.shape[1]
        self.faiss_index = faiss.IndexFlatL2(dimension)
        self.faiss_index.add(np.array(chunk_embeddings))
        self.chunks = chunks
    
    def answer_query(self, query: str, top_k: int = 5) -> str:
        """Answer question using RAG pipeline"""
        if not self.faiss_index:
            raise ValueError("Index not built. Load a PDF first.")
            
        query_embedding = self.embedder.encode([query])
        distances, indices = self.faiss_index.search(np.array(query_embedding), top_k)
        
        context = " ".join([self.chunks[idx] for idx in indices[0]])
        prompt = f"question: {query} context: {context} answer:"
        
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output_ids = self.gen_model.generate(
            input_ids, 
            max_length=256, 
            num_beams=10, 
            early_stopping=True
        )
        
        return self.tokenizer.decode(output_ids[0], skip_special_tokens=True)