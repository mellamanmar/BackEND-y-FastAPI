from fastapi import APIRouter,Path, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from service.movie_cast import Movie_castService
from config.database import Session
from schemas.movie_cast import Movie_cast


movie_cast_router =APIRouter()

@movie_cast_router.get('/movie_cast',tags=['movie_cast'],status_code=200)
def get_movie_cast():
    db = Session()
    result = Movie_castService(db).get_movie_cast()
    return JSONResponse (content=jsonable_encoder(result),status_code=200)

@movie_cast_router.get('/movie_cast_for_id',tags=['movie_cast'],status_code=200)
def get_movie_cast_for_id(id:int):
    db = Session()
    result = Movie_castService(db).get_for_id(id)
    return JSONResponse (content=jsonable_encoder(result), status_code=200)

@movie_cast_router.post('/movie_cast',tags=['movie_cast'],status_code=201)
def crete_movie_cast (movie_cast:Movie_cast):
    db = Session()
    Movie_castService(db).create_movie_cast(movie_cast)
    return JSONResponse (content={"menssage": "movie_cast created succesfully", "status_code": 201}, status_code= 201)

@movie_cast_router.put('/movie_cast{id}',tags=['movie_cast'])
def update_movie_cast(id:int,data:Movie_cast):
    db = Session()
    result = Movie_castService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={'message':"movie_cast don't found","status_code":404})
    Movie_castService(db).update_movie_cast(data)
    return JSONResponse(content={"message":"movie_cast updated succesfully", "status_code":200}, status_code=200)

@movie_cast_router.delete('/movie_cast{id}',tags=['movie_cast'])
def delete_movie_cast(id:int):
    db = Session()
    result = Movie_castService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={'message':"movie_cast don't gound","status_code":404})
    Movie_castService(db).delete_movie_cast(id)
    return JSONResponse(content={"message":"movie_cast delete succesfully", "status_code":200}, status_code=200)
