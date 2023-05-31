from fastapi import APIRouter,Path, Query,Depends
from fastapi.responses import  JSONResponse
from service.rating import  Ratingservice
from fastapi.encoders import jsonable_encoder

from fastapi.security import HTTPBearer
from config.database import Session
from models.rating import Rating as ratingModel
from service.rating import ratingService
from schemas.rating import Rating


rating_router=APIRouter()





@rating_router.get('/ratings',tags=['ratings'],response_model=list[Rating],status_code=200)
def get_ratings() -> Rating:
    db = Session()
    result = ratingService(db).get_rating()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@rating_router.get('/ratings/{id}',tags=['ratings'])
def get_rating(id:int = Path(ge=1,le=2000)):
    #Esta función tiene sólo una película por id
    db = Session()
    result = ratingService(db).get_rating(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)
    
@rating_router.get('/ratings/',tags=['ratings'],response_model=list[Rating],status_code=200)
def get_ratings_by_release_contry(release_contry:str = Query(min_length=3,max_length=15)):
    db = Session()
    result = db.query(ratingModel).filter(ratingModel.release_contry == release_contry).all()
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@rating_router.post('/ratings',tags=['ratings'],status_code=201,response_model=dict)
def create_rating(rating:Rating)->dict:
    db = Session()
    ratingService.create_rating(db,rating)
    return JSONResponse(content={"message":"Se ha registrado la pelicula","status_code":201})

@rating_router.put('/ratings{id}',tags=['ratings'])
def update_rating(id:int,rating:Rating):
    db =  Session
    result = ratingService(db).get_rating(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    ratingService(db).update_rating(id,rating)
    return JSONResponse(content={"message":"Se ha modificado la pelicula con id: {id}"})

   

@rating_router.delete('/ratings/{id}', tags=['ratings'], response_model=dict, status_code=200)
def delete_rating(id: int)-> dict:
    db = Session()
    result: ratingModel = db.query(ratingModel).filter(ratingModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    ratingService(db).delete_rating(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})