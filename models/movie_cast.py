from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Movie_cast(Base):
    __tablename__="movie_cast"

    id = Column(Integer,primary_key=True, index=True)  
    act_id = Column(Integer,ForeignKey("actor.id")) 
    mov_id = Column(Integer,ForeignKey("movie.id"))
    role = Column(String)
    
    actor = relationship("Actor", back_populates="movies_casts")
    movie = relationship("Movie", back_populates="movie_casts")
