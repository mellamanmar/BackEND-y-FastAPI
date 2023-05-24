from sqlalchemy import Column, Integer, String

from config.database import Base

class Actor(Base):
    __tablename__ ="actor"
    
    id = Column(Integer, primary_key = True)
    act_fname = Column(String)
    act_lname = Column(String)
    act_gender = Column(String)
