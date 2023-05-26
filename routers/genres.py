from fastapi import APIRouter,Path, Query
from fastapi.responses import HTMLResponse, JSONResponse


genres_router= APIRouter()

#función para verificar que está bien
@genres_router.get('/genres', tags=['genres'], status_code=200)
def get_router_hello():
    return HTMLResponse('<h1>Hola desde la ruta de genres</h1>')

@genres_router.get('/genres', tags=['genres'], status_code=200)
def get_genres():
    #función que trae todos los géneros que están en servicio
    return JSONResponse (content={"menssage": "estos son los géneros"})

@genres_router.post ('/genres', tags= 'genres', status_code=201)
def create_genres():
    #llamar a una función que va a estar en el servicio
    return JSONResponse (content={"menssage": "genres created succesfully"})

#para el genres delete debemos verificar que el id existe y después ese género lo eliminamos
# creamos un get que tare un sólo género por id (para crear las acciones put y delete)