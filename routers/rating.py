from fastapi import APIRouter, Path, Query
from fastapi.responses import  HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session
from service.rating import RatingService
from schemas.rating import Rating 

rating_router = APIRouter()

@rating_router.get('/rating', tags =['rating'], status_code = 200 )
def get_rating(): 
    db = Session()
    result = RatingService(db).get_rating()
    return JSONResponse (content = jsonable_encoder(result),status_code = 200)

@rating_router.get('/rating_for_id', tags = ['rating'], status_code = 200)
def get_id_reviewer(id:int): 
    db = Session()
    result = RatingService (db).get_rating_for_id(id)
    return JSONResponse (content = jsonable_encoder(result),status_code =200)

@rating_router.post('/rating', tags = ['rating'], status_code = 201 )
def create_rating(rating : Rating):     
    db = Session()
    RatingService(db).create_rating(rating)
    return JSONResponse (content = {'message': 'rating create succefully', 'status_code': 201}, status_code = 200)

@rating_router.put('/rating{id}',tags =['rating'])
def update_rating(id:int, data:Rating): 
    db = Session()
    result = RatingService (db).get_rating_for_id(id)
    if not result: 
        return JSONResponse (content = {'message': "rating don't found", 'status_code': 404 })
    RatingService(db).update_rating(data)
    return JSONResponse (content = {'message': 'rating update succesfully', 'status_code' : 200})

@rating_router.delete ('/rating{id}', tags =['rating'])
def delete_rating (id : int):
    db = Session()
    result = RatingService(db).get_rating_for_id(id)
    if not result: 
        return JSONResponse (content = {'message':"rating don't found", 'status_code': 404})
    RatingService(db).delete_rating(id)
    return JSONResponse(content={'message': 'rating deleted succesfully', 'status_code': 200}, status_code = 200 )
