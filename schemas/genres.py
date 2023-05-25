from pydantic import BaseModel,Field
from typing import Optional

class Genres(BaseModel):
    id : Optional[int] = None
    gen_title : str = Field(max_length=15,min_length=3, description="Pon el genero de la pelicula")
    
    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "gen_title":"Action"
            }
        }
