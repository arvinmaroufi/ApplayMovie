from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


STATUS = (
    ("draft", "پیش نویس شود"),
    ("published", "منتشر شود"),
)


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='نامک')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده مقاله')
    category = models.ManyToManyField(Category, related_name='articles', verbose_name='دسته بندی')
    title = models.CharField(max_length=200, unique=True, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, verbose_name='نامک')
    description = RichTextUploadingField(verbose_name='متن مقاله')
    thumbnail = models.ImageField(upload_to='article_thumbnails/', blank=True, null=True, verbose_name='تصویر مقاله')
    similar_articles = models.ManyToManyField('self', blank=True, null=True, related_name='similar', verbose_name='مقالات مشابه')
    status = models.CharField(choices=STATUS, max_length=10, default='published', verbose_name='وضعیت')
    views = models.IntegerField(default=0, verbose_name='بازدید ها')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ به‌روزرسانی')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comments', verbose_name='مقاله مربوطه')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_comments', verbose_name='نویسنده نظر')
    body = models.TextField(verbose_name='متن نظر')
    status = models.CharField(choices=STATUS, max_length=10, default='published', verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.article.title

