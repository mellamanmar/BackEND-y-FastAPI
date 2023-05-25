from pydantic import BaseModel,Field
from typing import Optional

class Actor(BaseModel):
    id : Optional[int] = None
    act_id : int = Field (ge=1,description="llave foranea de actor")
    mov_id :int = Field (ge=1,description="llave foranea de peliculas")
    role :str = Field (max_length=35,min_length=1,description="rol peliculas")
    class Config:
        schemas_extra= {
            "example":{
                "act_id":3,
                "mov_id":3,
                "role" :"michael"
            }
        }