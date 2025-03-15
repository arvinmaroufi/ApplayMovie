from django.urls import path
from . import views


app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('contact/', views.contact, name='contact'),
]

