from sqlalchemy import Column, ForeignKey , Integer

from config.database import Base

class Rating(Base):
    __tablename__ = "rating"

    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movie.id"))
    rev_id = Column(Integer, ForeignKey("user.id"))
    rev_stars = Column(Integer)
    num_o_ratings = Column(Integer)

#a 