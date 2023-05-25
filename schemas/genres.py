from pydantic import BaseModel, Field
from typing import Opcional

class Genres(BaseModel):
    id: Optiona[int]= None
    gen_title: str= Field(max_length=15, min_length=3, description="Género de la película")

    class Config:
        schema_extra= {
            "example":{
                "id":1, 
                "gen_title": "Drama"
            }
        }