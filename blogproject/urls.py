from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  
    path('video/' , include('video.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Apps4u.net AdminPanel"
admin.site.site_title = "Apps4u.net App Admin"
admin.site.site_index_title = "Welcome To Apps4u.net Admin Panel"

