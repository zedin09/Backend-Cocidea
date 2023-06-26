from sqlalchemy import Column, Integer, String, ARRAY
from config import Base

class Recipe(Base):
    __tablename__ = "recipe"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    ingredients = Column(ARRAY(String))
    duration = Column(String)
