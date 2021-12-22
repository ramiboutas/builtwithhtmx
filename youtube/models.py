from autoslug import AutoSlugField

from django.db import models


# The plan is to have a celery task that uses Youtube API to retrieve data from its server
# this retrieved data will be saved in our database (every 6 hours?)

class Video(models.Model):

    url = models.URLField()
    language = models.CharField(max_length=24)
    slug = models.SlugField() # channel name + video title + (year?)
    # duration =

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
