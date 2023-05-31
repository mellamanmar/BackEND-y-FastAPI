from fastapi import APIRouter,Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from service.director import DirectorService
from schemas.director import Director
from config.database import Session

director_router = APIRouter()


@director_router.get('/director', tags=['director'], status_code=200)
def get_director():
    db = Session()
    result = DirectorService(db).get_director()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@director_router.get('/director/{id}', tags=['director'], status_code=200)
def get_director_for_id(id: int):
    db = Session()
    result = DirectorService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)


@director_router.post('/director', tags=['director'], status_code=201)
def create_director(director:Director):
    db = Session()
    DirectorService(db).create_director(director)
    return JSONResponse(content={"message":" created successfully", "status_code" : 201})

@director_router.put("/director{id}",tags=["director"])
def update_director(id:int,director:Director):
    db = Session()
    result = DirectorService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"director dont't found", "status_code":404})
    DirectorService(db).update_director(director)
    return JSONResponse(content={"message":"director update succeefully","status_code":202}, status_code=202)
    
    
@director_router.delete("/director{id}",tags=["director"])
def delete_director(id:int,):
    db = Session()
    result = DirectorService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"director dont't found", "status_code":404})
    DirectorService(db).delete_director(id)
    return JSONResponse(content={"message":"director delete successfully", "status_code":200}, status_code=200)
