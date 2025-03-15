from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]