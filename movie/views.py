from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Series, Genre, Actor, MovieComment, SeriesComment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


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
    if request.method == 'POST':
        body = request.POST.get('body')
        MovieComment.objects.create(body=body, movie=movies, author=request.user)

    context = {
        'movies': movies,
    }
    return render(request, 'movie/movie_detail.html', context)


@login_required
def delete_movie_comment(request, comment_id):
    comment = get_object_or_404(MovieComment, id=comment_id, author=request.user)
    comment.delete()
    return redirect('movie:movie_detail', slug=comment.movie.slug)


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
    chapters = series.chapterseries_set.all()
    if request.method == 'POST':
        body = request.POST.get('body')
        SeriesComment.objects.create(body=body, series=series, author=request.user)

    context = {
        'series': series,
        'chapters': chapters,
    }
    return render(request, 'movie/series_detail.html', context)


@login_required
def delete_series_comment(request, comment_id):
    comment = get_object_or_404(SeriesComment, id=comment_id, author=request.user)
    comment.delete()
    return redirect('movie:series_detail', slug=comment.series.slug)


def genre_list(request):
    genres = Genre.objects.all()

    movie_genres_set = set()
    for movie in Movie.objects.prefetch_related('genre').distinct():
        for genre in movie.genre.all():
            movie_genres_set.add(genre)

    series_genres_set = set()
    for series in Series.objects.prefetch_related('genre').distinct():
        for genre in series.genre.all():
            series_genres_set.add(genre)

    context = {
        'genres': genres,
        'movie_genres': movie_genres_set,
        'series_genres': series_genres_set,
    }

    return render(request, 'movie/genre_list.html', context)


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


def actors_list(request):
    actors = Actor.objects.filter(status='published')
    page_number = request.GET.get('page')
    paginator = Paginator(actors, 12)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    context = {
        'actors': object_list,
        'pages_to_show': pages_to_show,
    }
    return render(request, 'movie/actors_list.html', context)


def actor_detail(request, slug):
    actors = get_object_or_404(Actor, slug=slug)
    movies = Movie.objects.filter(status='published', actors=actors)
    series = Series.objects.filter(status='published', actors=actors)
    items = list(movies) + list(series)
    actors.views += 1
    actors.save()
    context = {
        'actors': actors,
        'movies': movies,
        'series': series,
        'items': items,
    }
    return render(request, 'movie/actor_detail.html', context)


def search(request):
    query = request.GET.get('q')
    movies = Movie.objects.filter(title__icontains=query, status='published') if query else []
    series = Series.objects.filter(title__icontains=query, status='published') if query else []
    items = list(movies) + list(series)
    page_number = request.GET.get('page')
    paginator = Paginator(items, 4)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    context = {
        'query': query,
        'movies': movies,
        'series': series,
        'items': object_list,
        'pages_to_show': pages_to_show,
    }
    return render(request, 'movie/search_results.html', context)


def actor_search(request):
    actors_search = request.GET.get('actor')
    actors = Actor.objects.filter(status='published', name__icontains=actors_search)
    page_number = request.GET.get('page')
    paginator = Paginator(actors, 12)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    context = {
        'actors': object_list,
        'pages_to_show': pages_to_show,
    }
    return render(request, 'movie/actors_list.html', context)
