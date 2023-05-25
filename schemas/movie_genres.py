from pydantic import BaseModel, Field
from typing import Opcional

class MovieGenres(BaseModel):
    id: Opcional[int]= None
    gen_id: int= Field(ge=1, description= "id del género")
    movie_id= int= Field(ge=1, description= "llave foránea de películas")

    class Config: 
        schema_extra ={
            "example":{
                "id":1,
                "gen_id":2,
                "movie_id":3
            }
        }