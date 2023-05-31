from fastapi import FastAPI
from fastapi.responses import HTMLResponse


from config.database import engine,Base

from middlewares.error_handler import Errorhandler
from routers.movie import movie_router
from routers.genres import genres_router
from routers.actor import actor_router
from routers.movie_cast import movie_cast_router
from routers.director import director_router
from routers.movie_direction import movie_direction_router
from routers.reviewer import reviewer_router
from routers.rating import rating_router

app = FastAPI()
app.title = "Mi app con FastAPI"
app.version = "0.0.1"

app.add_middleware(Errorhandler)
app.include_router(movie_router)
app.include_router(genres_router)
app.include_router(actor_router)
app.include_router(movie_cast_router)
app.include_router(director_router)
app.include_router(movie_direction_router)
app.include_router(reviewer_router)
app.include_router(rating_router)

Base.metadata.create_all(bind=engine)


@app.get('/',tags=['home'],status_code=200)
def message():
    return HTMLResponse('<h1>Hello World</h1>')

@app.get('/hola',tags=['home'])
def hola():
    return HTMLResponse('<h1>Hola Clase</h1>')

