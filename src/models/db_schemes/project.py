from pydantic import BaseModel, Field, validator
from typing import Optional
from bson import ObjectId

class Project(BaseModel):
    id: Optional[ObjectId] = Field(default=None, alias="_id")
    project_id :str = Field(..., min_length=1)

    @validator("project_id")
    def validate_project_id(cls, value): #cls for static functions they don't receive any self -> object
        if not value.isalnum():
            raise ValueError("Project ID must be Alphanumeric")
        
        return value
    
    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def get_indexes(cls): # cls means it will refer to the class name -> Project 
        return [
            {
              "key": [
                ("project_id" ,1) # 1 for ascending 
              ],
              "name": "idx_project_id_1", # name of the index
              "unique" : True # ensure that each project has only one index
            }            
        ]
