from enum import Enum


class ResponseSignal(Enum):
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_TOO_LARGE = "file_size_too_large"
    FILE_UPLOADED_SUCCESSFULLY = "file_uploaded_successfully"
    FILE_UPLOADED_FAILED = "file_uploaded_failed"
    FILE_VALIDATED_SUCCESSFULLY = "file_validated_successfully"
    FILE_VALIDATED_FAILED = "file_validated_failed"
    FILE_PROCESSED_SUCCESSFULLY = "file_processed_successfully"
    FILE_PROCESSED_FAILED = "file_processed_failed"
    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"
