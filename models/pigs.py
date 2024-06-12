from.base import Base
class Pigs(Base, table=True):
    __tablename__= "pigs"
    
    name: str
    
    