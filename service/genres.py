from models.genres import Genres as GenresModel

class GenresService():
    def __init__(self,db):
        self.db = db
    
    def get_genres(self):
        result = self.db.query(GenresModel).all()
        return result
    
    def create_genre(self,genres:GenresModel):
        new_genre = GenresModel(
            gen_title = genres.gen_title.upper()
        )
        self.db.add(new_genre)
        self.db.commit()
        return
    
    def get_for_id(self,id:int):
        result = self.db.query(GenresModel).filter(GenresModel.id == id).first()
        return result
    