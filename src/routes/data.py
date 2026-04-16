from fastapi import APIRouter, FastAPI, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, Settings
from controllers import DataController
from controllers import ProjectController
import aiofiles
from models import ResponseSignal

data_router = APIRouter(prefix="/api/v1/data", tags=["api_v1", "data"])


@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id: str, file: UploadFile, app_settings: Settings = Depends(get_settings)
):

    # 1- validate file extension
    is_valid, message = DataController().validate_file(file=file)
    """if is_valid:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status": "success",
                "message": message,
                "data": {"is_valid": is_valid},
            },
        )
    # return {"status": "success","message": message,"data": {"is_valid": is_valid}}"""

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": "error",
                "message": message,
                "data": {"is_valid": is_valid},
            },
        )

    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path = os.path.join(
        project_dir_path,
        file.filename
    )
    async with aiofiles.open(file_path, "wb") as f:
        while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
            await f.write(chunk)

    return JSONResponse(
        content={
            "message": ResponseSignal.FILE_UPLOADED_SUCCESSFULLY.value,
        }
    )
