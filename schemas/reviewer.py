from pydantic import BaseModel, Field
from typing import Opcional

class Reviewer(BaseModel):
    id= Opcional[int]= None
    rev_name= str = Field(max_length= 100, min_length= 2, description= 'Name of reviewer')

    class Config:
        schema_extra= {
            "Example":{
                "id":1,
                "rev_name":"Righty Sock"
            }
        }