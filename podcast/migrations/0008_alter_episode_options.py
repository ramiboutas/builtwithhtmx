# Generated by Django 3.2.4 on 2021-08-14 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("podcast", "0007_alter_episode_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="episode", options={"ordering": ["created_datetime"]},
        ),
    ]
