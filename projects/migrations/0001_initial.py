# Generated by Django 3.2.9 on 2022-05-04 20:40

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('makers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('url', models.URLField(unique=True)),
                ('short_description', models.CharField(max_length=200)),
                ('user_email', models.EmailField(max_length=254)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title')),
                ('published', models.BooleanField(default=False)),
                ('is_open_source', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('homepage_screenshot', models.ImageField(blank=True, upload_to='website_homepage_screenshot/')),
                ('twitter_url', models.URLField(blank=True)),
                ('github_url', models.URLField(blank=True)),
                ('technology_suggestions_by_user', models.TextField(blank=True)),
                ('is_for_sale', models.BooleanField(default=False)),
                ('sale_link', models.URLField(blank=True)),
                ('additional_info', models.TextField(blank=True)),
                ('requirements', models.TextField(blank=True)),
                ('maker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='makers.maker')),
                ('technologies', models.ManyToManyField(blank=True, related_name='projects', to='projects.Technology')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(max_length=240)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='projects.project')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
    ]
