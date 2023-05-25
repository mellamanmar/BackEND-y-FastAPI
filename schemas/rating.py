from pydantic import BaseModel,Field
from typing import Optional

class Rating (BaseModel):
    id: Optional[int] = None
    movie_id: int = Field(min_length=1,max_length=10, description="Id de la pelicula")
    rev_id: int = Field(min_length=1,max_length=10, description="Id del usuario")
    rev_stars: int = Field(min_length=1,max_length=10, description="Calificacion")
    num_o_ratings: int = Field(min_length=1,max_length=10, description="Numero de calificaciones")

    class Config:
        schema_extra = {
            "example":{
                'id': 1,
                'movie_id': 1,
                'rev_id': 1,
                'rev_stars': 1,
                'num_o_ratings': 1,
            }
        }