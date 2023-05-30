from fastapi import APIRouter,Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from service.actor import ActorService
from config.database import Session
from fastapi.encoders import jsonable_encoder
from schemas.actor import Actor


actor_router=APIRouter()

@actor_router.get('/actor',tags=['actor'],status_code=200)
def get_actor():
    db = Session()
    result = ActorService(db).get_actor()
    return JSONResponse (content=jsonable_encoder(result), status_code=200)

@actor_router.get('/actor_for_id',tags=['actor'],status_code=200)
def get_actor_for_id(id:int):
    db = Session()
    result = ActorService(db).get_for_id(id)
    return JSONResponse (content=jsonable_encoder(result), status_code=200)

@actor_router.post('/actor',tags=['actor'],status_code=201)
def create_actor(actor:Actor):
    db = Session()
    ActorService(db).create_actor(actor)
    return JSONResponse (content={"menssage": "acotr created succesfully", "status_code": 201}, status_code= 201)

@actor_router.put('/actor{id}',tags=['actor'])
def update_actor(id:int,data:Actor):
    db = Session()
    result = ActorService(db).get_for_id(id)
    if not result:
        return JSONResponse(content= {"message":"actor don't found", "status_code":404})
    ActorService(db).update_actor(data)
    return JSONResponse(content={"message":"actor updated succesfully", "status_code":200}, status_code=200)

@actor_router.delete('/actor{id}',tags=['actor'])
def delete_actor(id:int,data:Actor):
    db = Session()
    result = ActorService(db).get_for_id(id)
    if not result:
        return JSONResponse(content= {"message":"actor don't gound", "status_code":404})
    ActorService(db).update_actor(data)
    return JSONResponse(content={"message":"actor delete succesfully", "status_code":200}, status_code=200)
