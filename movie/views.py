from django.shortcuts import render, get_object_or_404
from .models import Movie, Series, Genre


def movies_list(request):
    movies = Movie.objects.filter(status='published').order_by('-views')

    context = {
        'movies': movies
    }
    return render(request, 'movie/movies_list.html', context)


def movie_detail(request, slug):
    movies = get_object_or_404(Movie, slug=slug)
    movies.views += 1
    movies.save()

    context = {
        'movies': movies
    }
    return render(request, 'movie/movie_detail.html', context)


def series_list(request):
    series = Series.objects.filter(status='published').order_by('-views')

    context = {
        'series': series
    }
    return render(request, 'movie/series_list.html', context)


def series_detail(request, slug):
    series = get_object_or_404(Series, slug=slug)
    series.views += 1
    series.save()

    context = {
        'series': series
    }
    return render(request, 'movie/series_detail.html', context)


def genre_movies(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    movies = genre.movies_genre.filter(status='published')

    context = {
        'genre': genre,
        'movies': movies,
    }
    return render(request, 'movie/genre_movies.html', context)


def genre_series(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    series = genre.series_genre.filter(status='published')

    context = {
        'genre': genre,
        'series': series,
    }
    return render(request, 'movie/genre_series.html', context)
