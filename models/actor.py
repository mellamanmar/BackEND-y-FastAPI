from sqlalchemy import Column, Integer, String,ForeignKey
from config.database import Base
from sqlalchemy.orm import relationship

class Actor(Base):
    __tablename__ ="actor"
    
    id = Column(Integer, primary_key = True)
    act_fname = Column(String)
    act_lname = Column(String)
    act_gender = Column(String)

    movies_casts = relationship("Movie_cast", back_populates="actor", foreign_keys='Movie_cast.act_id')