from pydantic import BaseModel, Field
from typing import Opcional

class MovieDirection(BaseModel):
    id: Opcional[int]= None
    director_id: int= Field(ge=1, description= "llave foránea del director")
    movie_id= int= Field(ge=1, description= "llave foránea de películas")

    class Config:
        schema_extra= {
            "example":{
                "id":1,
                "director_id":2,
                "movie_id":3,
            }
        }