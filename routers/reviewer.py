from fastapi import APIRouter, Path, Query
from fastapi.responses import  HTMLResponse, JSONResponse
from service.reviewer import ReviewerService
from config.database import Session
from fastapi.encoders import jsonable_encoder
from schemas.reviewer import Reviewer

reviewer_router = APIRouter()

@reviewer_router.get('/reviewer', tags =['reviewer'], status_code = 200 )
def get_reviewer(): 
    db = Session()
    result = ReviewerService(db).get_reviewer()
    return JSONResponse (content = jsonable_encoder(result),status_code = 200)

@reviewer_router.get('/reviewer_for_id', tags = ['reviewer'], status_code = 200)
def get_id_reviewer(id:int): 
    db = Session()
    result = ReviewerService (db).get_reviewer_for_id(id)
    return JSONResponse (content = jsonable_encoder(result),status_code =200)

@reviewer_router.post('/reviewer', tags = ['reviewer'], status_code = 201 )
def create_reviewer(reviewer : Reviewer):     
    db = Session()
    ReviewerService(db).create_reviewer(reviewer)
    return JSONResponse (content = {'message': 'reviewer create succefully', 'status_code': 201}, status_code = 200)

@reviewer_router.put('/reviewer {id}',tags =['reviewer'])
def update_reviewer(id:int, data:Reviewer): 
    db = Session()
    result = ReviewerService (db).get_reviewer_for_id(id)
    if not result: 
        return JSONResponse (content = {'message': "reviewer don't found", 'status_code': 404 })
    ReviewerService(db).update_reviewer(data)
    return JSONResponse (content = {'message': 'reviewer update succesfully', 'status_code' : 200})

@reviewer_router.delete ('/reviewer{id}', tags =['reviewer'])
def delete_reviewer (id : int):
    db = Session()
    result = ReviewerService(db).get_reviewer_for_id(id)
    if not result: 
        return JSONResponse (content = {'message':"reviewer don't found", 'status_code': 404})
    ReviewerService(db).delete_reviewer(id)
    return JSONResponse(content={'message': 'reviewer deleted succesfully', 'status_code': 200}, status_code = 200 )
