from django.contrib import admin
from . import models
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(models.Category)
class CategoryAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'get_created_jalali']

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a، %d %b %Y')


@admin.register(models.Article)
class ArticleAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'views', 'get_created_jalali', 'status']
    list_editable = ['status']

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a، %d %b %Y')


@admin.register(models.ArticleComment)
class ArticleCommentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['article', 'author', 'short_body', 'get_created_at_jalali', 'status']
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
