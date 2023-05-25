from sqlalchemy import Column, ForeignKey, Integer

from config.database import Base

class MovieDirection(Base):

    __tablename__= "movie_direction"

    id= Column (Integer, primary_key=True)
    director_id= Column (Integer, ForeignKey("director.id"))
    movie_id= Column (Integer, ForeignKey("movie.id"))