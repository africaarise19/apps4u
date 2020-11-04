from django.urls import path
from .views import VideoListView, VideoDetailView

urlpatterns = [
    #path('', video),
    path('video/', VideoListView.as_view(), name="video_list"),
    path('details/<int:pk>', VideoDetailView.as_view(), name="video_detail"),
]