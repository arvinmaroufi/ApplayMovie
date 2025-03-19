from movie.models import Genre, Movie, Series
from core.models import SiteSettings
from blog.models import Article


def movie_func(request):
    site_settings = SiteSettings.objects.first()
    genres_movies = Genre.objects.all()
    genres_series = Genre.objects.all()
    popular_movies = Movie.objects.filter(status='published').order_by('-views')[:4]
    popular_series = Series.objects.filter(status='published').order_by('-views')[:4]
    return {
        'site_settings': site_settings,
        'genres_movies': genres_movies,
        'genres_series': genres_series,
        'popular_movies': popular_movies,
        'popular_series': popular_series,
    }


def blog_func(request):
    updated_articles = Article.objects.filter(status='published').order_by('-updated_at')[:4]
    popular_articles = Article.objects.filter(status='published').order_by('-views')[:4]
    return {
        'updated_articles': updated_articles,
        'popular_articles': popular_articles,
    }

