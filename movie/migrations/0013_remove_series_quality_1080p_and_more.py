# Generated by Django 5.1.7 on 2025-03-17 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0012_series_quality_1080p_series_quality_480p_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='quality_1080p',
        ),
        migrations.RemoveField(
            model_name='series',
            name='quality_480p',
        ),
        migrations.RemoveField(
            model_name='series',
            name='quality_720p',
        ),
        migrations.AddField(
            model_name='movie',
            name='quality_1080p',
            field=models.URLField(blank=True, null=True, verbose_name='لینک کیفیت 1080p'),
        ),
        migrations.AddField(
            model_name='movie',
            name='quality_480p',
            field=models.URLField(blank=True, null=True, verbose_name='لینک کیفیت 480p'),
        ),
        migrations.AddField(
            model_name='movie',
            name='quality_720p',
            field=models.URLField(blank=True, null=True, verbose_name='لینک کیفیت 720p'),
        ),
    ]
