from sqlalchemy import Column, Integer, String

from config.database import Base


class name (Base): #la verdad pense que era más largo ._.
    
    __tablename__ = "name"
    
    rev_Id = Column (Integer, prymary_key = True)
    rev_name = Column (String)