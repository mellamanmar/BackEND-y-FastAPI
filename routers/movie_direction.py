from fastapi import APIRouter,Path, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from service.movie_direction import Movie_directionService
from config.database import Session
from schemas.movie_direction import Movie_direction


movie_direction_router =APIRouter()

@movie_direction_router.get('/movie_direction',tags=['movie_direction'],status_code=200)
def get_movie_direction():
    db = Session()
    result = Movie_directionService(db).get_movie_direction()
    return JSONResponse (content=jsonable_encoder(result),status_code=200)

@movie_direction_router.get('/movie_direction_for_id',tags=['movie_direction'],status_code=200)
def get_movie_direction_for_id(id:int):
    db = Session()
    result = Movie_directionService(db).get_for_id(id)
    return JSONResponse (content=jsonable_encoder(result), status_code=200)

@movie_direction_router.post('/movie_direction',tags=['movie_direction'],status_code=201)
def crete_movie_direction(movie_direction:Movie_direction):
    db = Session()
    Movie_directionService(db).create_movie_direction(movie_direction)
    return JSONResponse (content={"menssage": "movie_direction created succesfully", "status_code": 201}, status_code= 201)

@movie_direction_router.put('/movie_direction{id}',tags=['movie_direction'])
def update_movie_direction(id:int,data:Movie_direction):
    db = Session()
    result = Movie_directionService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={'message':"movie_direction don't found","status_code":404})
    Movie_directionService(db).update_movie_cast(data)
    return JSONResponse(content={"message":"movie_direction updated succesfully", "status_code":200}, status_code=200)

@movie_direction_router.delete('/movie_direction{id}',tags=['movie_direction'])
def delete_movie_direction(id:int):
    db = Session()
    result = Movie_directionService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={'message':"movie_cast don't gound","status_code":404})
    Movie_directionService(db).delete_movie_direction(id)
    return JSONResponse(content={"message":"movie_direction delete succesfully", "status_code":200}, status_code=200)
