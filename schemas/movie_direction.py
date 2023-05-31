from pydantic import BaseModel, Field
from typing import Optional

class Movie_direction(BaseModel):
    id: Optional[int]= None
    director_id : int= Field(ge=1, description= "llave foránea del director")
    movie_id : int= Field(ge=1, description= "llave foránea de películas")

    class Config:
        schema_extra= {
            "example":{
                "director_id":2,
                "movie_id":3,
            }
        }