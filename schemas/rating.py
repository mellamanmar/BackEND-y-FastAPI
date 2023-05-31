from pydantic import BaseModel,Field
from typing import Optional

class Rating (BaseModel):
    id: Optional[int] = None
    movie_id: int = Field(ge=1, description="llave foranea de la pelicula")
    rev_id: int = Field(ge=1, description="lleve foranea del usuario")
    rev_stars: float = Field(le=10)
    num_o_ratings: int = Field(ge=1)

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