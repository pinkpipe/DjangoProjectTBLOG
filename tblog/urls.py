from django.urls import path
from . import views

app_name = 'tblog'

urlpatterns = [
    path('', views.first_list, name='first_list'),
    path('auth/register/', views.register_user, name='register'),
    path('auth/login/', views.login_user, name='login'),
]