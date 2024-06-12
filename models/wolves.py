from.base import Base
class Wolves(Base, table=True):
    __tablename__= "wolves"
    
    name: str
    
    