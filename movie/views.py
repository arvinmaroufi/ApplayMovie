from django.shortcuts import render, get_object_or_404
from .models import Movie, Series, Genre
from django.core.paginator import Paginator


def get_pages_to_show(current_page, total_pages):
    if total_pages <= 3:
        return list(range(1, total_pages + 1))

    if current_page <= 2:
        return [1, 2, 3, '...', total_pages]

    if current_page >= total_pages - 1:
        return [1, '...', total_pages - 2, total_pages - 1, total_pages]

    return [1, '...', current_page - 1, current_page, current_page + 1, '...', total_pages]


def movies_list(request):
    movies = Movie.objects.filter(status='published').order_by('-views')
    page_number = request.GET.get('page')
    paginator = Paginator(movies, 4)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    context = {
        'movies': object_list,
        'pages_to_show': pages_to_show,
    }
    return render(request, 'movie/movies_list.html', context)


def movie_detail(request, slug):
    movies = get_object_or_404(Movie, slug=slug)
    movies.views += 1
    movies.save()

    context = {
        'movies': movies,
    }
    return render(request, 'movie/movie_detail.html', context)


def series_list(request):
    series = Series.objects.filter(status='published').order_by('-views')
    page_number = request.GET.get('page')
    paginator = Paginator(series, 4)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    context = {
        'series': object_list,
        'pages_to_show': pages_to_show,
    }
    return render(request, 'movie/series_list.html', context)


def series_detail(request, slug):
    series = get_object_or_404(Series, slug=slug)
    series.views += 1
    series.save()

    context = {
        'series': series,
    }
    return render(request, 'movie/series_detail.html', context)


def genre_movies(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    movies = genre.movies_genre.filter(status='published')
    page_number = request.GET.get('page')
    paginator = Paginator(movies, 4)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    context = {
        'genre': genre,
        'movies': object_list,
        'pages_to_show': pages_to_show,
    }
    return render(request, 'movie/genre_movies.html', context)


def genre_series(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    series = genre.series_genre.filter(status='published')
    page_number = request.GET.get('page')
    paginator = Paginator(series, 4)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    context = {
        'genre': genre,
        'series': object_list,
        'pages_to_show': pages_to_show,
    }
    return render(request, 'movie/genre_series.html', context)
