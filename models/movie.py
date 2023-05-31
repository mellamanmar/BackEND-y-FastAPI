from sqlalchemy import Column,Integer, String, Float,ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Movie(Base):

    __tablename__ = "movie"

    id = Column(Integer,primary_key = True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    time = Column(Float)
    date_release = Column(String)
    release_contry = Column(String)

    movie_casts = relationship("Movie_cast", foreign_keys="[Movie_cast.mov_id]", back_populates="movie")