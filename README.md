# 🚀 Mini-RAG

A modular, lightweight **Retrieval-Augmented Generation (RAG)** backend application built with **FastAPI**, **LangChain**, and **MongoDB**. It provides an end-to-end foundation to ingest, validate, chunk, and store documents (PDF, TXT) scoped by project for LLM-powered question answering.

---

## ✨ Features

- **⚡ Fast & Asynchronous**: Built with FastAPI and Motor (async MongoDB driver) for high-performance non-blocking I/O.
- **📁 Project-Isolated Storage**: Ingested files and database records are partitioned cleanly by `project_id`.
- **📄 Multi-Format Document Ingestion**: Upload and validate `.pdf` (via PyMuPDF) and `.txt` documents with strict MIME type and file size limits.
- **✂️ Customizable Text Chunking**: Semantic and recursive splitting using LangChain's `RecursiveCharacterTextSplitter` with customizable `chunk_size` and `chunk_overlap`.
- **🗄️ Database Persistence**: Automatic project registration and bulk insertion of processed text chunks into MongoDB (`projects` and `chunks` collections).
- **🐳 Dockerized Database**: Effortless container orchestration for MongoDB with data persistence and custom port mapping.
- **📖 Auto-Generated API Docs**: Interactive Swagger UI and ReDoc endpoints available out of the box.

---

## 🏗️ Project Architecture

```
Mini-RAG/
├── docker/
│   ├── docker-compose.yml       # MongoDB Docker Compose configuration
│   ├── .env.example             # Docker environment variables template
│   ├── .env                     # Docker environment variables (local)
│   └── mongodb_data/            # Persistent storage volume for MongoDB
├── src/
│   ├── assets/files/            # Local storage for uploaded project documents
│   ├── controllers/             # Business logic layer
│   │   ├── BaseController.py    # Common paths and helper utilities
│   │   ├── DataController.py    # File validation & naming logic
│   │   ├── ProcessController.py # Document loading (PyMuPDF/Text) & text chunking
│   │   └── ProjectController.py # Project directory manager
│   ├── helpers/
│   │   └── config.py            # Pydantic Settings configuration loader
│   ├── models/                  # Database models and data access layer
│   │   ├── BaseDataModel.py     # Base DB client wrapper
│   │   ├── ChunkModel.py        # Chunk database operations (bulk write, delete)
│   │   ├── ProjectModel.py      # Project collection operations
│   │   ├── db_schemes/          # Pydantic & BSON document schemes
│   │   └── enums/               # Application enums
│   ├── routes/                  # FastAPI routers and request schemas
│   │   ├── base.py              # Base health check routes
│   │   ├── data.py              # File upload & document processing endpoints
│   │   └── schemes/             # Request payload schemas
│   ├── main.py                  # Application entry point & MongoDB lifecycle
│   ├── requirements.txt         # Python package dependencies
│   ├── .env.example             # Application environment template
│   └── .env                     # Application environment configuration (local)
├── LICENSE
└── README.md
```

---

## 📋 System Requirements

- **Operating System**: Windows, Linux, or macOS
- **Python**: 3.11 or higher
- **Docker & Docker Compose**: Installed and running ([Docker Desktop](https://www.docker.com/products/docker-desktop/))
- **RAM**: Minimum 4 GB (8 GB+ recommended)

---

## 🐳 Docker Setup (MongoDB)

Mini-RAG uses Docker to run a containerized **MongoDB 9.0** database with persistent local storage.

### 1. Configure Docker Environment Variables
Navigate to the `docker/` folder and create a `.env` file from `.env.example`:

```bash
cd docker
cp .env.example .env
```

Ensure your `docker/.env` contains the desired root credentials:
```env
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=admin
```

### 2. Service Specifications
The `docker/docker-compose.yml` configures:
- **Image**: `mongo:9.0.2-noble`
- **Container Name**: `mongodb`
- **Port Mapping**: `27007:27017` (Maps container port `27017` to host port `27007` to avoid port collisions)
- **Persistent Volume**: `./mongodb_data:/data/db` (Data persists across restarts)
- **Restart Policy**: `always`

### 3. Manage the Database Container

Run these commands from the project root:

- **Start the MongoDB container (detached mode)**:
  ```bash
  docker compose -f docker/docker-compose.yml up -d --build
  ```

- **Verify the container is running**:
  ```bash
  docker compose -f docker/docker-compose.yml ps
  ```

- **Inspect MongoDB container logs**:
  ```bash
  docker compose -f docker/docker-compose.yml logs -f mongodb
  ```

- **Stop the container**:
  ```bash
  docker compose -f docker/docker-compose.yml stop
  ```

- **Stop and remove container & networks**:
  ```bash
  docker compose -f docker/docker-compose.yml down
  ```

---

## 🚀 Application Installation & Setup

### 1. Python Environment Setup

We recommend using [Miniconda](https://docs.anaconda.com/miniconda/) or Python `venv`:

#### Using Miniconda:
```powershell
# Create a virtual environment
conda create -n mini-rag python=3.11 -y

# Activate the environment
conda activate mini-rag
```

#### Using Python venv:
```bash
python -m venv venv

# On Linux / macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 2. Install Python Dependencies
Install the required packages from `src/requirements.txt`:

```bash
pip install -r src/requirements.txt
```

### 3. Configure Application Environment Variables
Navigate to the `src/` directory and create the `.env` file from `src/.env.example`:

```bash
cd src
cp .env.example .env
```

Edit `src/.env` to configure your settings:

```env
APP_NAME="Mini-RAG"
APP_VERSION="0.0.1"
OPENAI_API_KEY="your-openai-api-key-here"

# Allowed MIME types for document uploads
FILE_ALLOWED_EXTENSIONS=["text/plain", "application/pdf"]

# Maximum allowed upload file size in Megabytes
FILE_MAX_SIZE=10

# Streaming upload chunk size in bytes (512 KB)
FILE_DEFAULT_CHUNK_SIZE=512000

# MongoDB Connection (matches Docker host port 27007)
MONGODB_URL="mongodb://localhost:27007"
MONGODB_DATABASE="mini-rag"
```

> **Note**: If running FastAPI inside WSL2 or a separate VM connecting to Docker on Windows, replace `localhost` in `MONGODB_URL` with your host IP address.

---

## ▶️ Running the Application

1. **Make sure your MongoDB container is running**:
   ```bash
   docker compose -f docker/docker-compose.yml up -d
   ```

2. **Start the FastAPI server with Uvicorn**:
   ```bash
   cd src
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Access Interactive API Documentation**:
   - **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
   - **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔌 API Endpoints Reference

### 1. Welcome / Health Check
- **Endpoint**: `GET /api/v1/`
- **Description**: Returns basic application metadata and status.
- **Example Response**:
  ```json
  {
    "message": "Welcome to Mini-RAG version 0.0.1"
  }
  ```

---

### 2. Upload Document
- **Endpoint**: `POST /api/v1/data/upload/{project_id}`
- **Description**: Validates MIME type and file size, generates a unique file identifier, creates/retrieves the project in MongoDB, and saves the file under `src/assets/files/{project_id}/`.
- **Form Data**:
  - `file`: Multipart file (`.txt` or `.pdf`, max 10MB)
- **Example cURL**:
  ```bash
  curl -X POST "http://localhost:8000/api/v1/data/upload/projectA" \
       -H "accept: application/json" \
       -H "Content-Type: multipart/form-data" \
       -F "file=@sample.pdf"
  ```
- **Example Response**:
  ```json
  {
    "message": "file_uploaded_successfully",
    "file_id": "aB1cD2eF3gH4_sample.pdf"
  }
  ```

---

### 3. Process & Chunk Document
- **Endpoint**: `POST /api/v1/data/process/{project_id}`
- **Description**: Loads the document using PyMuPDF (PDF) or TextLoader (TXT), splits it into chunks via `RecursiveCharacterTextSplitter`, and performs bulk insertion into MongoDB.
- **JSON Request Body**:
  ```json
  {
    "file_id": "aB1cD2eF3gH4_sample.pdf",
    "chunk_size": 100,
    "chunk_overlap": 20,
    "do_reset": 0
  }
  ```
  - `file_id` *(string, required)*: The unique file identifier returned from the upload endpoint.
  - `chunk_size` *(int, optional)*: Maximum characters per chunk (default: `100`).
  - `chunk_overlap` *(int, optional)*: Character overlap between consecutive chunks (default: `20`).
  - `do_reset` *(int, optional)*: Set to `1` to purge prior chunks for this project before inserting new ones (default: `0`).
- **Example Response**:
  ```json
  {
    "message": "file_processed_successfully",
    "file_id": "aB1cD2eF3gH4_sample.pdf",
    "chunk_size": 100,
    "chunk_overlap": 20,
    "Inserted_chunks": 42
  }
  ```

---

## 🛠️ Troubleshooting & Helpful Tips

- **Container Port Already in Use**:
  If port `27007` is in use, modify the host port in `docker/docker-compose.yml` (e.g. `"27008:27017"`) and update `MONGODB_URL` in `src/.env` accordingly.
- **Viewing Database Data**:
  You can connect to your running database with MongoDB Compass or VS Code MongoDB extension using:
  ```
  mongodb://localhost:27007
  ```
- **WSL2 / Windows Host IP Resolution**:
  When running the server in WSL2 and Docker on Windows, use `hostname -I` to discover the internal WSL IP if binding `0.0.0.0` or testing network connections between interfaces.

---

## 📄 License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.
