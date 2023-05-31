from models.movie_direction import Movie_direction as Movie_directionModel
from schemas.movie_direction import Movie_direction as Movie_directionSchema

class Movie_directionService():
    def __init__(self,db):
        self.db = db

    def get_movie_direction(self):
        result = self.db.query(Movie_directionModel).all()
        return result

    def create_movie_direction(self, movie_direction:Movie_directionModel):
        new_movie_direction = Movie_directionModel(
            director_id= movie_direction.director_id,
            movie_id= movie_direction.movie_id
        )
        self.db.add(new_movie_direction)
        self.db.commit()
        return

    def get_for_id(self, id:int):
        result = self.db.query(Movie_directionModel).filter(Movie_directionModel.id == id).first()
        return result

    def update_movie_direction(self,data:Movie_directionModel):
        movie_direction = self.db.query(Movie_directionModel).filter(Movie_directionModel.id == data.id).first()
        movie_direction.director_id = data.director_id
        movie_direction.movie_id = data.movie_id
        self.db.commit()        
        return

    def delete_movie_direction(self, id:int):
        self.db.query(Movie_directionModel).filter(Movie_directionModel.id == id).delete()
        self.db.commit()
        