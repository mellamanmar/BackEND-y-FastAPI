from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from service.director import DirectorService
from config.database import Session
from fastapi.encoders import jsonable_encoder
from schemas.director import Director

director_router = APIRouter()

#
#
#
#


@director_router.get('/director', tags=['director'], status_code=200)
def get_director():
    #
    db = Session()
    result = DirectorService(db).get_directors()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@director_router.get('/director/{id}', tags=['director'], status_code=200)
def get_director_by_id(id: int):
    db = Session()
    result = DirectorService(db).get_director_by_id(id)
    if not result:
        return JSONResponse(content={"message": "Director not found", "status_code": 404})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@director_router.post('/director', tags=['director'], status_code=201)
def create_director(director: Director):
    db = Session()
    DirectorService(db).create_director(director)
    return JSONResponse(content={"message": "Director created successfully", "status_code": 201}, status_code=201)

@director_router.put('/director/{id}', tags=['director'])
def update_director(id: int, data: Director):
    db = Session()
    result = DirectorService(db).get_director_by_id(id)
    if not result:
        return JSONResponse(content={"message": "Director not found", "status_code": 404})
    DirectorService(db).update_director(data)
    return JSONResponse(content={"message": "Director updated successfully", "status_code": 200}, status_code=200)

@director_router.delete('/director/{id}', tags=['director'])
def delete_director(id: int):
    db = Session()
    result = DirectorService(db).get_director_by_id(id)
    if not result:
        return JSONResponse(content={"message": "Director not found", "status_code": 404})
    DirectorService(db).delete_director(id)
    return JSONResponse(content={"message": "Director deleted successfully", "status_code": 200}, status_code=200)

#
#