from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base 

class Director(Base):
    __tablename__ = "director"
    
    id = Column(Integer,primary_key = True)
    dir_fname = Column(String)
    dir_lname = Column(String)
    
    movie_directions = relationship("Movie_direction",back_populates="director", foreign_keys='Movie_direction.director_id')
    