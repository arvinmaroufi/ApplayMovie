from django.db import models
from django.contrib.auth.models import User
import os


GENDER = (
    ("man", "مرد"),
    ("woman", "زن"),
)

STATUS = (
    ("draft", "پیش نویس شود"),
    ("published", "منتشر شود"),
)


class Genre(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='عنوان ژانر')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='نامک')
    thumbnail = models.ImageField(upload_to='genre_thumbnails/', null=True, blank=True, verbose_name='تصویر ژانر')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'ژانر'
        verbose_name_plural = 'ژانر ها'

    def __str__(self):
        return self.title


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='زبان')

    class Meta:
        verbose_name = 'زبان'
        verbose_name_plural = 'زبان ها'

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='اسم بازیگر')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='نامک')
    description = models.TextField(verbose_name='درباره بازیگر')
    thumbnail = models.ImageField(upload_to='actor_thumbnails/', null=True, blank=True, verbose_name='تصویر بازیگر')
    gender = models.CharField(choices=GENDER, max_length=10, default='man', verbose_name='جنسیت')
    date_birth = models.DateField(verbose_name='تاریخ تولد')
    place_birth = models.CharField(max_length=300, verbose_name='محل تولد')
    views = models.IntegerField(default=0, verbose_name='بازدید ها')
    status = models.CharField(choices=STATUS, max_length=10, default='published', verbose_name='وضعیت')

    class Meta:
        verbose_name = 'بازیگر'
        verbose_name_plural = 'بازیگران'

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='عنوان فیلم')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='نامک')
    genre = models.ManyToManyField(Genre, related_name='movies_genre', verbose_name='ژانر')
    language = models.ManyToManyField(Language, related_name='movies_language', verbose_name='زبان فیلم')
    description = models.TextField(verbose_name='خلاصه داستان')
    thumbnail = models.ImageField(upload_to='movie_thumbnails/', null=True, blank=True, verbose_name='تصویر فیلم')
    actors = models.ManyToManyField(Actor, related_name='movies', verbose_name='بازیگران')
    similar_movies = models.ManyToManyField('self', blank=True, null=True, related_name='similar', verbose_name='فیلم های مشابه')
    country = models.CharField(max_length=300, verbose_name='کشور سازنده')
    director = models.CharField(max_length=200, verbose_name='اسم کارگردان')
    duration = models.CharField(max_length=5, verbose_name='مدت زمان فیلم (لطفاً مدت زمان را به دقیقه وارد کنید)')
    release_date = models.DateField(verbose_name='تاریخ انتشار')
    score = models.CharField(max_length=10, default='0.0/10', verbose_name='امتیاز')
    age_range = models.CharField(max_length=20, default='بالای 14 سال', verbose_name='رنج سنی')
    views = models.IntegerField(default=0, verbose_name='بازدید ها')
    trailer = models.URLField(max_length=500, verbose_name='لینک تریلر فیلم')
    subtitle_url = models.URLField(max_length=500, blank=True, null=True, verbose_name='لینک زیرنویس فیلم')
    quality_480p = models.URLField(verbose_name='لینک کیفیت 480p', blank=True, null=True)
    quality_720p = models.URLField(verbose_name='لینک کیفیت 720p', blank=True, null=True)
    quality_1080p = models.URLField(verbose_name='لینک کیفیت 1080p', blank=True, null=True)
    is_recommended = models.BooleanField(default=False, verbose_name='آیا فیلم، پیشنهادی است؟')
    status = models.CharField(choices=STATUS, max_length=10, default='published', verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ به‌روزرسانی')

    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم ها'

    def formatted_release_date(self):
        return self.release_date.strftime('%Y/%m/%d')

    def __str__(self):
        return self.title


def movie_image_upload_to(instance, filename):
    movie_slug = instance.movie.slug
    folder_name = f"movie_images/{movie_slug}/"
    return os.path.join(folder_name, filename)


class MovieImage(models.Model):
    movie = models.ForeignKey(Movie, related_name="movie_images", on_delete=models.CASCADE, verbose_name='فیلم مربوطه')
    images = models.ImageField(upload_to=movie_image_upload_to, null=True, blank=True, verbose_name='اسکرین شات فیلم')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = "تصویر فیلم"
        verbose_name_plural = "تصاویر فیلم ها"


class Series(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='عنوان سریال')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='نامک')
    genre = models.ManyToManyField(Genre, related_name='series_genre', verbose_name='ژانر')
    language = models.ManyToManyField(Language, related_name='series_language', verbose_name='زبان سریال')
    description = models.TextField(verbose_name='خلاصه داستان')
    thumbnail = models.ImageField(upload_to='series_thumbnails/', null=True, blank=True, verbose_name='تصویر سریال')
    actors = models.ManyToManyField(Actor, related_name='series', verbose_name='بازیگران')
    similar_series = models.ManyToManyField('self', blank=True, null=True, related_name='similar', verbose_name='سریال های مشابه')
    country = models.CharField(max_length=300, verbose_name='کشور سازنده')
    director = models.CharField(max_length=200, verbose_name='اسم کارگردان')
    duration = models.CharField(max_length=5, verbose_name='مدت زمان سریال (لطفاً مدت زمان را به دقیقه وارد کنید)')
    chapter_count = models.PositiveIntegerField(verbose_name='تعداد فصل ها')
    release_date = models.DateField(verbose_name='تاریخ انتشار')
    score = models.CharField(max_length=10, default='0.0/10', verbose_name='امتیاز')
    age_range = models.CharField(max_length=20, default='بالای 14 سال', verbose_name='رنج سنی')
    views = models.IntegerField(default=0, verbose_name='بازدید ها')
    trailer = models.URLField(max_length=500, verbose_name='لینک تریلر سریال')
    subtitle_url = models.URLField(max_length=500, blank=True, null=True, verbose_name='لینک زیرنویس سریال')
    status = models.CharField(choices=STATUS, max_length=10, default='published', verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ به‌روزرسانی')

    class Meta:
        verbose_name = 'سریال'
        verbose_name_plural = 'سریال ها'

    def formatted_release_date(self):
        return self.release_date.strftime('%Y/%m/%d')

    def __str__(self):
        return self.title


def series_image_upload_to(instance, filename):
    series_slug = instance.series.slug
    folder_name = f"series_images/{series_slug}/"
    return os.path.join(folder_name, filename)


class SeriesImage(models.Model):
    series = models.ForeignKey(Series, related_name="series_images", on_delete=models.CASCADE, verbose_name='سریال مربوطه')
    images = models.ImageField(upload_to=series_image_upload_to, null=True, blank=True, verbose_name='اسکرین شات سریال')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = "تصویر سریال"
        verbose_name_plural = "تصاویر سریال ها"


class ChapterSeries(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, verbose_name='سریال مربوطه')
    title = models.CharField(max_length=150, unique=True, verbose_name='عنوان فصل')
    order = models.PositiveIntegerField(verbose_name='ترتیب فصل')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ به‌روزرسانی')

    class Meta:
        verbose_name = 'فصل سریال'
        verbose_name_plural = 'فصل های سریال'

    def __str__(self):
        return self.title


class VideoSeries(models.Model):
    chapter = models.ForeignKey(ChapterSeries, on_delete=models.CASCADE, verbose_name='فصل مربوطه')
    quality_480p = models.URLField(verbose_name='لینک کیفیت 480p', blank=True, null=True)
    quality_720p = models.URLField(verbose_name='لینک کیفیت 720p', blank=True, null=True)
    quality_1080p = models.URLField(verbose_name='لینک کیفیت 1080p', blank=True, null=True)
    order = models.PositiveIntegerField(verbose_name='ترتیب ویدیو')

    class Meta:
        verbose_name = 'ویدیو سریال'
        verbose_name_plural = 'ویدیو های سریال'

    def __str__(self):
        return self.chapter.title


class MovieComment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_comments', verbose_name='فیلم مربوطه')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movie_comments', verbose_name='نویسنده نظر')
    body = models.TextField(verbose_name='متن نظر')
    status = models.CharField(choices=STATUS, max_length=10, default='published', verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'نظر فیلم'
        verbose_name_plural = 'نظرات فیلم ها'

    def __str__(self):
        return self.movie.title


class SeriesComment(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name='series_comments', verbose_name='سریال مربوطه')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='series_comments', verbose_name='نویسنده نظر')
    body = models.TextField(verbose_name='متن نظر')
    status = models.CharField(choices=STATUS, max_length=10, default='published', verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'نظر سریال'
        verbose_name_plural = 'نظرات سریال ها'

    def __str__(self):
        return self.series.title
