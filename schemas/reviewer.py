from pydantic import BaseModel, Field
from typing import Optional

class Reviewer(BaseModel):
    id : Optional[int]= None
    rev_name: str = Field(max_length= 100, min_length= 2, description= 'Name of reviewer')

    class Config:
        schema_extra= {
            "example":{
                "id":1,
                "rev_name":"Righty Sock"
            }
        }