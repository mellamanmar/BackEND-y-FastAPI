from models.rating import Rating as RatingModel
from schemas.rating import Rating


class Ratingservice():

    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(RatingModel).all()
        return result

    def get_movie(self, id: int):
        result = self.db.query(RatingModel).filter(RatingModel.id == id).first()
        return result

    def get_movies_rating(self, release_country: str):
        result = self.db.query(RatingModel).filter(RatingModel.release_country == release_country).all()
        return result        

    def create_rating(self, movie: Rating):
        new_rate = RatingModel(
            title=movie.title,
            overview=movie.overview,
            year=movie.year,
            time=movie.time,
            date_release=movie.date_release,
            movie_cast_id=movie.movie_cast_id,
            release_country=movie.release_country,
            rating_stars=movie.rating_stars       
        )
        self.db.add(new_rate)
        self.db.commit()

    def update_rate(self, id: int, data: Rating):
        movie = self.db.query(RatingModel).filter(RatingModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.time = data.time
        movie.date_release = data.date_release
        movie.release_country = data.release_country
        movie.rating_stars = data.rating_stars
        self.db.commit()

    def delete_rate(self, id: int):
        self.db.query(RatingModel).filter(RatingModel.id == id).delete()
        self.db.commit()