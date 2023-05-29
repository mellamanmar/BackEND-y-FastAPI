from fastapi import APIRouter,Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from service.genres import GenresService
from config.database import Session
from fastapi.encoders import jsonable_encoder
from schemas.genres import Genres

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
def create_genres(genres: Genres):
    #llamar a una función que va a estar en el servicio
    db= Session()
    GenresService(db).create_genre(genres)
    return JSONResponse (content={"menssage": "genre created succesfully", "status_code": 201}, status_code= 201)

@genres_router.put('/genres{id}', tags= ['genres'])
def update_genre(id:int,data:Genres):
    db= Session()
    result= GenresService(db).get_for_id(id)
    if not result:
        return JSONResponse(content= {"message":"genre don't found", "status_code":404})
    GenresService(db).update_genre(data)
    return JSONResponse(content={"message":"genre updated succesfully", "status_code":200}, status_code=200)

@genres_router.delete('/genres{id}', tags=['genres'])
def delete_genre(id:int):
    db= Session()
    result= GenresService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"genre don't found", "status_code":404})
    GenresService(db).delete_genre(id)
    return JSONResponse (content={"message": "genre deleted succesfully", "status_code ":200}, status_code=200 )

#para el genres delete debemos verificar que el id existe y después ese género lo eliminamos
# creamos un get que tare un sólo género por id (para crear las acciones put y delete)

@genres_router.put('/genres{id}',tags=['genres'])
def update_genre(id:int,data:Genres):
    db = Session()
    result = GenresService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={'message':"genre don't gound","status_code":404})
    GenresService(db).update_genre(data)
    return JSONResponse (content={"menssage": "genre created succesfully", "status_code": 202}, status_code= 202)

@genres_router.delete('/genres{id}',tags=['genres'])
def delete_genre(id:int):
    db = Session()
    result = GenresService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={'message':"genre don't gound","status_code":404})
    GenresService(db).delete_genre(id)
    return JSONResponse (content={"menssage": "genre delete succesfully", "status_code": 200}, status_code= 200)
