from fastapi import APIRouter,Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from service.genres import GenresService
from config.database import Session
from fastapi.encoders import jsonable_encoder
from schemas.genres import Genres as GenresSchema

genres_router= APIRouter()

# #función para verificar que está bien
# @genres_router.get('/genres_hello', tags=['genres'], status_code=200)
# def get_genres_hello():
#     return HTMLResponse('<h1>Hola desde la ruta de genres</h1>')
    

@genres_router.get('/genres', tags=['genres'], status_code=200)
def get_genres():
    #función que trae todos los géneros que están en servicio
    db= Session()
    result = GenresService(db).get_genres()
    return JSONResponse (content=jsonable_encoder(result), status_code=200)

@genres_router.get('/genres_for_id', tags=['genres'], status_code=200)
def get_genres_fot_id(id:int):
    db= Session()
    result= GenresService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@genres_router.post ('/genres', tags= ['genres'], status_code=201)
def create_genres(genres: GenresSchema):
    #llamar a una función que va a estar en el servicio
    db= Session()
    GenresService(db).create_genre(genres)
    return JSONResponse (content={"menssage": "genre created succesfully", "status_code": 201}, status_code= 201)

#para el genres delete debemos verificar que el id existe y después ese género lo eliminamos
# creamos un get que tare un sólo género por id (para crear las acciones put y delete)