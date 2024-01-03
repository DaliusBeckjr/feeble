# server urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('apps.user.urls')),
    path('movies/', include('apps.movie.urls')),
]
