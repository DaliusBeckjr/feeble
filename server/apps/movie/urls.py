# movies urls.py

from django.urls import path
# from django.conf.urls import handler404
from . import views
# from apps.movie.views import not_found

app_name = 'movies'

# handler404 = not_found

urlpatterns = [
    # movies/ 
    path('', views.dashboard, name= 'dashboard'),
    path('new/', views.add_movie, name= 'new'),

    path('<int:movie_id>/', views.display, name = 'one_movie'),
    path('<int:movie_id>/edit/', views.update, name = 'edit'),
    path('<int:movie_id>/delete/', views.delete, name = 'delete'), 
    
    path('404/', views.not_found, name = '404')
]