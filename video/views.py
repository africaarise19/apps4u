from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

# def video(request):
#     obj=Item.objects.all()
#     return render(request, 'video.html', {'obj':obj}) 

class VideoListView(ListView):
    model = Item
    template_name = 'video_list.html'
    ordering = ['-post_date']
    paginate_by = 5

class VideoDetailView(DetailView):
    model = Item
    template_name = 'video_detail.html'
    

