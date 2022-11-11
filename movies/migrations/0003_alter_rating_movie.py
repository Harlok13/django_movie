# Generated by Django 4.1.3 on 2022-11-08 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_alter_category_url_alter_movie_actors_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rating",
            name="movie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="movies.movie",
                verbose_name="Фильм",
            ),
        ),
    ]