from sqlalchemy import Column, ForeignKey , Integer,Float

from config.database import Base

class Rating(Base):
    __tablename__ = "rating"

    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movie.id"))
    rev_id = Column(Integer, ForeignKey("reviewer.id"))
    rev_stars = Column(Float)
    num_o_ratings = Column(Integer)

