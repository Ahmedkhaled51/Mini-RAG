from .BaseController import BaseController
from .ProjectController import ProjectController
import os
from langchain_community.document_loaders import TextLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from models import ProcessingEnum


class ProcessController(BaseController):
    def __init__(self, project_id: str):
        super().__init__()
        self.project_id = project_id
        self.project_dir_path = ProjectController().get_project_path(
            project_id=project_id
        )

    def get_file_extension(self, file_id: str) -> str:
        return os.path.splitext(file_id)[-1]

    def get_file_loder(self, file_id: str):
        file_ext = self.get_file_extension(file_id=file_id)
        file_path = os.path.join(self.project_dir_path, file_id)
        if file_ext == ProcessingEnum.TXT.value:
            return TextLoader(file_path, encoding="utf-8")
        elif file_ext == ProcessingEnum.PDF.value:
            return PyMuPDFLoader(file_path)
        return None

    def get_file_content(self, file_id: str):
        file_loder = self.get_file_loder(file_id=file_id)
        if file_loder:
            return file_loder.load()
        return None

    def process_file_content(
        self, file_content: list, file_id: str, chunk_size=100, chunk_overlap=20
    ):
        text_splitter = RecursiveCharacterTextSplitter(
            separators=[
                "\n\n",
                "\n",
                ".",
                " ",
            ],  # separator order (most specific first)
            chunk_size=chunk_size,  # max size of each chunk (characters)
            chunk_overlap=chunk_overlap,  # overlap between chunks (characters) to maintain context
            length_function=len,  # function to measure length (default: len())
            is_separator_regex=False,  # whether separators are regular expressions
        )

        file_content_texts = [rec.page_content for rec in file_content]

        file_content_metadata = [rec.metadata for rec in file_content]

        chunks = text_splitter.create_documents(
            file_content_texts, metadatas=file_content_metadata
        )
        return chunks
