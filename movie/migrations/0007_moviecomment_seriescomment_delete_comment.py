# Generated by Django 5.1.7 on 2025-03-17 19:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_rename_movie_genre_movie_genre_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='متن نظر')),
                ('status', models.CharField(choices=[('draft', 'پیش نویس شود'), ('published', 'منتشر شود')], default='published', max_length=10, verbose_name='وضعیت')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_comments', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده نظر')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_comments', to='movie.movie', verbose_name='فیلم مربوطه')),
            ],
            options={
                'verbose_name': 'نظر فیلم',
                'verbose_name_plural': 'نظرات فیلم ها',
            },
        ),
        migrations.CreateModel(
            name='SeriesComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='متن نظر')),
                ('status', models.CharField(choices=[('draft', 'پیش نویس شود'), ('published', 'منتشر شود')], default='published', max_length=10, verbose_name='وضعیت')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series_comments', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده نظر')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series_comments', to='movie.series', verbose_name='سریال مربوطه')),
            ],
            options={
                'verbose_name': 'نظر سریال',
                'verbose_name_plural': 'نظرات سریال ها',
            },
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
