from.base import Base 
from sqlmodel import Field 
from sqlalchemy import Boolean

class Houses(Base, table=True):
    __tablename__= "houses"
    
    material: str
    pig_id:int | None = Field(default=None, foreign_key="pigs.id")
    attacked: bool = Field (sa_column=Boolean(), default=False)
    
    