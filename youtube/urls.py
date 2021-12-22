from django.urls import path

from .views import VideoListView, VideoDetailView

app_name = 'youtube'

urlpatterns = [
    path('list/', VideoListView.as_view(), name='list'),
    path('video/<slug:slug>/', VideoDetailView.as_view(), name='detail'),
]
