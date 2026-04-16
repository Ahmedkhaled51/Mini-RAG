from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, Settings
from controllers import DataController
from controllers import ProjectController
import aiofiles
from models import ResponseSignal
import logging 


logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(prefix="/api/v1/data", tags=["api_v1", "data"])


@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id: str, file: UploadFile, app_settings: Settings = Depends(get_settings)
):

    # 1- validate file extension
    data_controller = DataController()


    is_valid, message = data_controller.validate_file(file=file)
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
    file_path = data_controller.generate_unique_file_name(orig_file_name=file.filename, project_id=project_id)

    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error uploading file: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": ResponseSignal.FILE_UPLOAD_FAILED.value,
                "message": str(e),
                "data": {"is_valid": False},
            },
        )

    return JSONResponse(
        content={
            "message": ResponseSignal.FILE_UPLOADED_SUCCESSFULLY.value,
        }
    )
