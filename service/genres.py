from models.genres import Genres as GenresModel
from schemas.genres import Genres as GenresSchema

class GenresService():
    def __init__(self, db):
        self.db = db
    
    def get_genres(self):
        result= self.db.query(GenresModel).all()
        return result

    def create_genre(self, genre: GenresModel):
        new_genre= GenresModel(
            gen_title= genre.gen_title.upper()
        )
        self.db.add(new_genre)
        self.db.commit()
        return
    
    def get_for_id (self, id:int):
        result= self.db.query(GenresModel).filter(GenresModel.id == id).first()
        return result

    def update_genre(self, data:GenresModel):
        genre= self.db.query(GenresModel).filter(GenresModel.id == data.id).first()
        genre.gen_title= data.gen_title
        self.db.commit()
        return 

    def delete_genre(self, id:int):
        self.db.query(GenresModel). filter(GenresModel.id == id). delete()
        self.db.commit()
        