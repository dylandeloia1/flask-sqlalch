
from src.models import db, Movie

class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
        movies = Movie.query.all()
        return movies

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        movie = Movie.query.filter_by(movie_id=movie_id).first()
        print(movie.title)
        return movie

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        movie = Movie(title=title, director=director, rating=rating)
        db.session.add(movie)
        db.session.commit()
        return movie


    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        movies = Movie.query.filter(Movie.title.ilike(f'%{title}%')).all()
        return movies


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
