from django.urls import path
from login_system import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/users/', views.search_users, name='search_users'),
]
