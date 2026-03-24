# Mini-RAG

A lightweight Retrieval-Augmented Generation (RAG) application designed to allow you to chat with your data using Large Language Models (LLMs).

## Requirements
- python 3.8 or higher
- #### How to install python using miniconda
1) download miniconda from [here](https://www.anaconda.com/docs/getting-started/miniconda/install/overview)
2) create a virtual environment using the following command:
    ```bash
    $ conda create -n rag python=3.8
    ```
3) activate the virtual environment using the following command:
    ```bash
    $ conda activate mini-rag
    ```  

### System Requirements
- Operating System: Windows / Linux / macOS
- Python 3.8+ 
- Minimum 4GB RAM (8GB+ recommended if running local models)

### Prerequisites
Before running this project, you will need:
- Optional: An API key for your chosen LLM (e.g., OpenAI API Key) if you are not using a local, open-source model.
- (If using local models): [Ollama](https://ollama.com/) or similar local inference engine installed.
- Git for version control.

## ✨ Features

- **Document Ingestion**: Supports uploading and parsing various document formats (PDF, TXT, CSV, Markdown).
- **Text Chunking**: Efficiently splits documents into logical chunks for better embedding and retrieval.
- **Vector Database**: Utilizes a fast and scalable vector database (e.g., ChromaDB or FAISS) for storing document embeddings locally.
- **Semantic Search**: Accurately retrieves contextually relevant information from your documents based on user queries.
- **LLM Integration**: Seamlessly generates natural and precise answers citing your specific data.

## 🛠️ Tech Stack

- **Language**: Python
- **LLM Framework**: LangChain or LlamaIndex
- **Embeddings**: HuggingFace (local) or OpenAI
- **Vector Store**: ChromaDB
- **User Interface**: Streamlit (or FastAPI for a backend-only approach)

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Mini-RAG.git
   cd Mini-RAG
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   # (Note: make sure to create a requirements.txt file)
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Create a `.env` file in the root directory and add any necessary API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 🎯 Usage

To start the Mini-RAG system, run the main application:

```bash
# Example if using Streamlit:
streamlit run app.py

# Example if running a terminal application:
python main.py
```

1. Add your documents via the UI or place them into a designated `data/` folder.
2. The system will process, chunk, and index the documents into the vector database.
3. You can now use the chat interface to ask questions about your uploaded documents!

## 📁 Project Structure

```text
Mini-RAG/
├── data/               # Folder for storing raw documents to be indexed
├── vectorstore/        # Local persistent directory for ChromaDB/FAISS
├── src/                # Main source code
│   ├── ingestion.py    # Logic for reading and chunking documents
│   ├── embedding.py    # Logic for generating vectors
│   ├── retrieval.py    # Logic for searching the vector database
│   └── generation.py   # Logic for LLM system prompt and response
├── app.py              # Main entry point for the application (e.g., Streamlit UI)
├── requirements.txt    # Project Python dependencies
├── .env.example        # Example environment variables required
└── README.md           # Project documentation
```

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features you'd like to add.
