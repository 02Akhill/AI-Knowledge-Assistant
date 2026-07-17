# AI Knowledge Assistant

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask natural language questions based on their content.

## Features

- Upload multiple PDF documents
- Extract text using PyMuPDF
- Intelligent text chunking
- Gemini Embeddings
- ChromaDB vector database (Coming Soon)
- Semantic search (Coming Soon)
- AI-powered question answering (Coming Soon)
- React frontend (Coming Soon)

## Tech Stack

### Backend
- Python 3.12
- FastAPI
- Google Gemini
- PyMuPDF
- ChromaDB
- LangChain Text Splitters

### Frontend
- React
- Vite
- Tailwind CSS

## Current Progress

- ✅ PDF Upload
- ✅ Multi PDF Upload
- ✅ Text Extraction
- ✅ Page Metadata
- ✅ Chunking
- ✅ Document Processing Pipeline
- ✅ Gemini Embeddings
- ⏳ ChromaDB Integration
- ⏳ Semantic Search
- ⏳ Chat API
- ⏳ React Frontend

## Run

```bash
python -m uvicorn backend.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

## Author

Akhil S