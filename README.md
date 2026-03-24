# Mini-RAG

A lightweight Retrieval-Augmented Generation (RAG) application designed to allow you to chat with your data using Large Language Models (LLMs).

## Requirements
- python 3.8 or higher
- #### How to install python using miniconda
1) download miniconda from [here](https://www.anaconda.com/docs/getting-started/miniconda/install/overview)
2) create a virtual environment using the following command:
    ```powershell
    $ conda create -n rag python=3.8
    ```
3) activate the virtual environment using the following command:
    ```powershell
    $ conda activate mini-rag
    ```  

### System Requirements
- Operating System: Windows / Linux / macOS
- Python 3.8+ 
- Minimum 4GB RAM (8GB+ recommended if running local models)

## 🚀 Installation & Setup
1. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Environment Variables:**
   Create a `.env` file in the root directory and add any necessary API keys like `OPENAI_API_KEY`
   ```bash
   cp .env.example .env
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
