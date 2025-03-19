from django.urls import path
from . import views


app_name = 'movie'
urlpatterns = [
    path('movies/', views.movies_list, name='movies_list'),
    path('movies/<slug:slug>/', views.movie_detail, name='movie_detail'),
    path('movie_comment/delete/<int:comment_id>/', views.delete_movie_comment, name='delete_movie_comment'),
    path('series/', views.series_list, name='series_list'),
    path('series/<slug:slug>/', views.series_detail, name='series_detail'),
    path('series_comment/delete/<int:comment_id>/', views.delete_series_comment, name='delete_series_comment'),
    path('genres/', views.genre_list, name='genre_list'),
    path('genre/movies/<slug:slug>/', views.genre_movies, name='genre_movies'),
    path('genre/series/<slug:slug>/', views.genre_series, name='genre_series'),
    path('actors/', views.actors_list, name='actors_list'),
    path('actors/<slug:slug>/', views.actor_detail, name='actor_detail'),
    path('search/', views.search, name='search'),
    path('actor_search/', views.actor_search, name='actor_search'),
]
