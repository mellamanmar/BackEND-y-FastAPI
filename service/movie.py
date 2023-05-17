from models.movie import Movie as MovieModel
from schemas.movie import Movie


class MovieService():

    def __init__(self,db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result

    def get_movie(self,id:int):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result

    def get_movies_by_release_contry(self,release_contry:str):
        result = self.db.query(MovieModel).filter(MovieModel.release_contry == release_contry).all()
        return result        

    def create_movie(self, movie:Movie):
        new_movie = MovieModel(
        title=movie.title,
        overview = movie.overview,
        year = movie.year,
        time = movie.time,
        date_release = movie.date_release,
        release_contry = movie.release_contry
        )
        self.db.add(new_movie)
        self.db.commit()
        return 

    def update_movie(self,id:int, data:Movie):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.time = data.time
        movie.date_release = data.date_release
        movie.release_contry = data.release_contry
        self.db.commit()
        return


    def delete_movie(self, id: int):
       self.db.query(MovieModel).filter(MovieModel.id == id).delete()
       self.db.commit()
       return


