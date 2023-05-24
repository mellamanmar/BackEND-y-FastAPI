from sqlalchemy import Column, Integer, String

from config.database import Base

<<<<<<< HEAD
class Genres(Base):
    
    __tablename__ ="genres"
    
    id = Column(Integer,primary_key=True)
    gen_title = Column(String)
=======
class Genres (Base):
    __tablename__ = "genres"

    id= Column(Integer, primary_key=True)
    gen_title= Column(String)
>>>>>>> main
