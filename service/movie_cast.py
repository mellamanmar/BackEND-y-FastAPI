from models.movie_cast import Movie_cast as Movie_castModel
from schemas.movie_cast import Movie_cast as Movie_castSchema

class Movie_castService():
    def __init__(self,db):
        self.db = db

    def get_movie_cast(self):
        result = self.db.query(Movie_castModel).all()
        return result

    def create_movie_cast(self, movie_cast:Movie_castModel):
        new_movie_cast = Movie_castModel(
            act_id = movie_cast.act_id,
            mov_id= movie_cast.mov_id,
            role = movie_cast.role.upper()
        )
        self.db.add(new_movie_cast)
        self.db.commit()
        return

    def get_for_id(self, id:int):
        result = self.db.query(Movie_castModel).filter(Movie_castModel.id == id).first()
        return result

    def update_actor(self,data:Movie_castModel):
        movie_cast = self.db.query(Movie_castModel).filter(Movie_castModel.id == data.id).first()
        movie_cast.act_id = data.act_id
        movie_cast.mov_id = data.mov_id
        movie_cast.role = data.role
        self.db.commit()        
        return

    def delete_movie_cast(self, id:int):
        self.db.query(Movie_castModel).filter(Movie_castModel.id == id).delete()
        self.db.commit()
