# Generated by Django 3.2.4 on 2021-08-13 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("podcast", "0004_episode_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="episode", name="show_notes", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="episode", name="slug", field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name="episode",
            name="thumbnail",
            field=models.ImageField(upload_to="podcast_episode_thumbnail/"),
        ),
        migrations.AlterField(
            model_name="episode", name="transcript", field=models.TextField(),
        ),
    ]
