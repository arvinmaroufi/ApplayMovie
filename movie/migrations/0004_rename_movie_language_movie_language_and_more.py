# Generated by Django 5.1.7 on 2025-03-15 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_alter_series_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movie_language',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='series_language',
            new_name='language',
        ),
    ]
