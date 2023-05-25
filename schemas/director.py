from pydantic import BaseModel, Field
from typing import Opcional

class Director(BaseModel):
    id = Opcional[int]= None
    dir_fname = str = Field(max_length = 30, min_length = 2, description="First Name of Director")
    dir_lname = str = Field(max_length = 50, min_length = 3, description="Last Name of director")

    class Config:
        schema_extra = {
            "Example":{
                "id":1,
                "dir_fname" : "Alfred",
                "dir_lname" : "Hitchcock",
            }
        }