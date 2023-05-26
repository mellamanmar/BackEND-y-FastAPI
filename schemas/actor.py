from pydantic import BaseModel,Field
from typing import Optional

class Actor(BaseModel):
    id : Optional[int] = None
    act_fname : str = Field(max_length=22, min_length= 3, description="nombre o nombres del actor")
    act_lname : str = Field(max_length=22, min_length= 3, description="apellido o apellidos del actor")
    act_gender : str = Field(max_length=12, min_length= 2, description="genero del actor")
    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "act_fname":"jason",
                "act_lname":"momoa",
                "act_gender":"M"
            }
        }