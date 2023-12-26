from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name="all_movies"),
    path('new', views.add_movie, name="new_movie"),
    path('<int:movie_id>', views.display, name="display_movie"),
    path('<int:movie_id>/edit', views.update_movie, name="update"),
]