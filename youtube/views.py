from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Video

class VideoListView(ListView):
    model = Video

class VideoDetailView(DetailView):
    model = Video
