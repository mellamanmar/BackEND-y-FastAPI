# Proyecto de CRUD de Películas - FastAPI

<img src="img/programate-academy.png" alt="Logo Programate">

## Descripción

Este proyecto es un ejemplo de una API RESTful desarrollada con FastAPI que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en un modelo de películas. Está diseñado con un enfoque académico para que los aprendices de programación backend puedan utilizarlo como punto de partida y comenzar a trabajar sobre él.

## Funcionalidades

- Obtener todas las películas disponibles
- Obtener una película por su ID
- Crear una nueva película
- Actualizar una película existente
- Eliminar una película

## Tecnologías utilizadas

- Python
- FastAPI
- Pydantic

## Instalación

1. Clona este repositorio en tu máquina local:

git clone git@github.com:JSand89/my-movie-app-c9.git


2. Navega al directorio del proyecto:

cd my-movie-app-c9

3. Tu o uno de tus companeros debe cambiar el origen del repositorio 

git remote -v

git remote remove origin

git remote add origin <nueva_url_del_repositorio>

4. Ahora, tus compañeros deben clonar tu repositorio y tú debes darles permiso para editarlo

Desde el repositorio en GitHub, ve a "Settings" y luego a la sección de "Collaborators" para agregarlos. Esto tiene como objetivo permitirles realizar cambios. No te preocupes, realizaremos este proceso en clase."

5. Instala las dependencias necesarias:

pip install -r requirements.txt


## Uso

1. Inicia la aplicación:

uvicorn main:app --reload


2. Accede a la documentación de la API en tu navegador:

http://localhost:8000/docs


3. Prueba las diferentes rutas disponibles para realizar operaciones CRUD en las películas.


## Contacto

Si tienes alguna pregunta o sugerencia o quieres el workbook para desarrollar este proyecto, no dudes en contactarme en [jsanchez@educamas.com.co](jsanchez@educamas.com.co).


