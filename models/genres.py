from sqlalchemy import Column, String, Integer

from config.database import Base

class genre (Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key = True)
    gen_ttile= Column(String)