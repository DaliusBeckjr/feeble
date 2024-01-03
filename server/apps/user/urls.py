from django.urls import path
from apps.user import views 

app_name = 'users'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    
    path('logout', views.logout, name = 'logout'),
]