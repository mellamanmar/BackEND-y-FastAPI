from pydantic import BaseModel, Field
from typing import Optional 

class Movie(BaseModel):
        id: Optional[int] = None
        title: str = Field(max_length=15,min_length=3)
        overview: str = Field(max_length=300,min_length=10)
        year: int = Field(le=2023)
        time: float = Field(ge=1,le=1000)
        date_release : str  = Field(max_length=15,min_length=3)
        release_contry: str = Field(max_length=15,min_length=3)

        class Config:
            schema_extra = {
                "example":{
                    'id': 1,
                    'title': 'Avatar',
                    'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
                    'year':2002,
                    'time': 1.50,
                    'date_release':'2009',
                    'release_contry':'USA',
                }
            }

