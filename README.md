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

## Run the FastAPI server
```powershell
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
