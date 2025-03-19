from django.contrib import admin
from . import models
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


class MovieImageAdmin(admin.TabularInline):
    model = models.MovieImage


class SeriesImageAdmin(admin.TabularInline):
    model = models.SeriesImage


class VideoSeriesAdmin(admin.TabularInline):
    model = models.VideoSeries


@admin.register(models.Genre)
class MovieGenreAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'get_created_at_jalali']

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_at_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a، %d %b %Y')


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'date_birth', 'place_birth', 'views', 'status']
    search_fields = ['name']
    list_editable = ['status']


@admin.register(models.Movie)
class MovieAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['short_title', 'country', 'director', 'duration', 'release_date', 'score', 'age_range', 'views', 'get_created_at_jalali', 'status']
    inlines = [MovieImageAdmin]
    search_fields = ['title']
    list_editable = ['status']

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_at_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a، %d %b %Y')

    def short_title(self, obj):
        if len(obj.title) > 20:
            return obj.title[:20] + '...'
        return obj.title
    short_title.short_description = 'عنوان فیلم'


@admin.register(models.Series)
class SeriesAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['short_title', 'country', 'director', 'duration', 'release_date', 'score', 'age_range', 'views', 'get_created_at_jalali', 'status']
    inlines = [SeriesImageAdmin]
    search_fields = ['title']
    list_editable = ['status']

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_at_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a، %d %b %Y')

    def short_title(self, obj):
        if len(obj.title) > 20:
            return obj.title[:20] + '...'
        return obj.title
    short_title.short_description = 'عنوان سریال'


@admin.register(models.ChapterSeries)
class ChapterSeriesAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['series', 'title', 'order', 'get_created_at_jalali']
    inlines = [VideoSeriesAdmin]

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_at_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a، %d %b %Y')


@admin.register(models.MovieComment)
class MovieCommentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['movie', 'author', 'short_body', 'get_created_at_jalali', 'status']
    list_filter = ['status']
    list_editable = ['status']

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_at_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a، %d %b %Y - %H:%M:%S')

    def short_body(self, obj):
        if len(obj.body) > 20:
            return obj.body[:20] + '...'
        return obj.body
    short_body.short_description = 'متن نظر'


@admin.register(models.SeriesComment)
class SeriesCommentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['series', 'author', 'short_body', 'get_created_at_jalali', 'status']
    list_filter = ['status']
    list_editable = ['status']

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_at_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a، %d %b %Y - %H:%M:%S')

    def short_body(self, obj):
        if len(obj.body) > 20:
            return obj.body[:20] + '...'
        return obj.body
    short_body.short_description = 'متن نظر'

