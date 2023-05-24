from sqlalchemy import Column, ForeignKey, Integer

from config.database import Base

class MovieGenres(Base):

    __tablename__= "movie_genres"

    id= Column (Integer, primary_key=True)
    gen_id= Column (Integer, ForeignKey("genre.id"))
    movie_id= Column (Integer, FForeignKey("movie.id"))

    
