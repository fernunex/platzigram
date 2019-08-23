"""Platzi URLs module."""

#Django
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin




    


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include(('posts.urls','posts'),namespace='posts')),

    path('users/', include(('profile_user.urls', 'profile_user'),namespace='users'))
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
