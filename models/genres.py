from sqlalchemy import Column, String, Integer
from config.database import Base

class Genres(Base):
    
    __tablename__ ="genres"
    
    id = Column(Integer,primary_key=True)
    gen_title = Column(String)
