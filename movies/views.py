import movies as movies
from django.shortcuts import render
from django.views import View

from movies.models import Movie


class MoviesView(View):
    """Список фильмов"""
    def get(self, request,):
        movies = Movie.objects.all()
        return render(request, "movies/movies.html", {"movie_list": movies})
