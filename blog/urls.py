from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
    path('article_comment/delete/<int:comment_id>/', views.delete_article_comment, name='delete_article_comment'),
    path('category/<slug:slug>/', views.article_category, name='article_category'),
]
