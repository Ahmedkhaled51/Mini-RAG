from pydantic import BaseModel, Field, validator
from typing import Optional
from bson import ObjectId
from datetime import datetime


class Asset(BaseModel):
    id: Optional[ObjectId] = Field(default=None, alias="_id")
    asset_project_id: ObjectId
    asset_type: str = Field(..., min_length=1)
    asset_name: str = Field(..., min_length=1)
    asset_size: int = Field(ge=0, default=None)
    asset_cofig: dict = Field(default=None)
    asset_pushed_at: datetime = Field(default=datetime.utcnow)

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def get_indexes(cls):  # cls means it will refer to the class name -> Asset
        return [
            {
                "key": [("asset_project_id", 1)],  # 1 for ascending
                "name": "idx_asset_project_id_1",  # name of the index
                "unique": False,  # ensure that each project has only one index
            },
            {
                "key": [("asset_project_id", 1), ("asset_name", 1)],
                "name": "idx_asset_project_id_name_1",  # name of the index
                "unique": True,  # ensure that each project has only one index
            },
        ]
