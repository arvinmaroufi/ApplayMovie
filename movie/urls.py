from django.urls import path
from . import views


app_name = 'movie'
urlpatterns = [
    path('movies/', views.movies_list, name='movies_list'),
    path('movies/<slug:slug>/', views.movie_detail, name='movie_detail'),
    path('series/', views.series_list, name='series_list'),
    path('series/<slug:slug>/', views.series_detail, name='series_detail'),
    path('genre/movies/<slug:slug>/', views.genre_movies, name='genre_movies'),
    path('genre/series/<slug:slug>/', views.genre_series, name='genre_series'),
]
