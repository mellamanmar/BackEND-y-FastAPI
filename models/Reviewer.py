from sqlalchemy import Column, Integer, String

from config.database import Base


class Reviewer(Base): #la verdad pense que era más largo ._.
    
    __tablename__ = "reviewer"
    
    id = Column (Integer, primary_key = True)
    rev_name = Column (String)