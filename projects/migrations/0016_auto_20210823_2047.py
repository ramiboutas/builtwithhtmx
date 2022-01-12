# Generated by Django 3.2.4 on 2021-08-23 20:47

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0015_alter_like_author"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="website_additional_info",
            new_name="additional_info",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="website_description",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="website_github",
            new_name="github_url",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="website_homepage_screenshot",
            new_name="homepage_screenshot",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="website_requirements",
            new_name="requirements",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="website_short_description",
            new_name="short_description",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="website_title",
            new_name="title",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="website_twitter",
            new_name="twitter_url",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="website_url",
            new_name="url",
        ),
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                always_update=True, editable=False, populate_from="title"
            ),
        ),
    ]