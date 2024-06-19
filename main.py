import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware 
from sqlmodel import Session, select, func
from db import get_session 
from models.pigs import Pigs
from models.wolves import Wolves
from models.houses import Houses
from models.attacks import Attacks 


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials= True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/houses')
def get_houses(session: Session = Depends(get_session)):
    statement = select(
        Houses.id,
        Houses.material,
        Houses.attacked,
        func.array_agg(Pigs.name).label('piggies')
    ).join (
        Pigs, Pigs.id == Houses.pig_id
    ).group_by(
        Houses
    )
    results = session.exec(statement).mappings().all ()
    return results



if __name__== '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
    
    
    
@app.post('/pigs/add')
async def add_pig(name:str, session: Session= Depends(get_session)):
    piglet = Pigs(name=name) #insert into pigs table value for the column name that is name will see this in swagger 
    session.add(piglet) #executes the insert 
    session.commit()#opens connection to database runs sequal runs response then get return -- always do this if its non GET
    return {"Piglet Added":piglet.name}

@app.post('/wolves/add')
def add_wolf(wolf:Wolves, session:Session = Depends(get_session)):
    wolf=Wolves(name=wolf.name)
    session.add(wolf)
    session.commit()
    return{"Wolf Added": wolf.name}

@app.post('/houses/add')
def add_house(material: str, pig_id: int, attacked: bool, session: Session = Depends(get_session)):
    house = Houses(material=material, pig_id=pig_id, attacked = attacked)
    session.add(house)
    session.commit()
    return{"House added", house.material}
    