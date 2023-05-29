from models.movie_direction import MovieDirection as MovieDirectionModel
from schemas.movie_direction import MovieDirection as MovieDirectionSchema



class MovieDirectionService():
    def __init__(self, db):
        self.db= db

    def get_movie_direction(self):
        result= self.db.query(MovieDirectionModel).all()
        return result

    def get_for_id(self, id:int):
        result= self.db.query(MovieDirectionModel).filter(MovieDirectionModel.id == id).first()
        return result

    def create_movie_direction (self, mdrelation: MovieDirectionModel):
        new_relation= MovieDirectionModel(
            director_id= mdrelation.director_id
        )
        self.db.add(new_relation)
        self.db.commit()
        return