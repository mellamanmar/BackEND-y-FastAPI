from sqlalchemy import Column, ForeingKey, Integer

from config import Base

class MovieGenres(Base):

    __tablename__= "movie_genres"

    id= Column (Integer, primary_key=True)
    gen_id= Column (Integer, ForeingKey("genre.id"))
    movie_id= Column (Integer, ForeingKey("movie.id"))

    
