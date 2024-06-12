from.base import Base
from sqlmodel import Field
from sqlalchemy import Boolean

class Attacks(Base, table=True):
    __tablename__= "attacks"
    
    name: str
    wolf_id: int | None= Field(default=None, foreign_key="wolves.id")
    house_id: int | None=Field(default=None, foreign_key="houses.id")
    successful: bool = Field(sa_column=Boolean(), default=False) 
    
    
    