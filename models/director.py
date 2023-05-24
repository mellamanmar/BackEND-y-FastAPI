from sqlalchemy import Column, Integer, String

from config.database import Base 

class Director(Base):
    
    __tablename__ = "Director"
    
    id = Column(Integer,primary_key = True)
    dir_fname = Column(String)
    dir_lname = Column(String)
    