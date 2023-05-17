from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from fastapi.security import HTTPBearer
from config.database import Session
from models.movie import Movie as MovieModel
from service.movie import MovieService
from schemas.movie import Movie


movie_router = APIRouter()




#@app.get('/movies',tags=['movies'],response_model=List[Movie],status_code=200, dependencies=[Depends(JWYBearer())])
@movie_router.get('/movies',tags=['movies'],response_model=List[Movie],status_code=200)
def get_movies() -> Movie:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_router.get('/movies/{id}',tags=['movies'])
def get_movie(id:int = Path(ge=1,le=2000)):
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)
    
@movie_router.get('/movies/',tags=['movies'],response_model=List[Movie],status_code=200)
def get_movies_by_release_contry(release_contry:str = Query(min_length=3,max_length=15)):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.release_contry == release_contry).all()
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_router.post('/movies',tags=['movies'],status_code=201,response_model=dict)
def create_movie(movie:Movie)->dict:
    db = Session()
    MovieService.create_movie(db,movie)
    return JSONResponse(content={"message":"Se ha registrado la pelicula","status_code":201})

@movie_router.put('/movies{id}',tags=['movies'])
def update_movie(id:int,movie:Movie):
    db =  Session
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    MovieService(db).update_movie(id,movie)
    return JSONResponse(content={"message":"Se ha modificado la pelicula con id: {id}"})

   

@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int)-> dict:
    db = Session()
    result: MovieModel = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})