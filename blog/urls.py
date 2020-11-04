from django.urls import path
from . import views
from .views import HomeView, BlogDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('blog/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
    path('search/', views.search, name='search'),
       
]
