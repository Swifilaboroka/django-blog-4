from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('categories/<int:pk>/', views.category, name='post_list'),
    path('posts/<str:slug>/', views.article_page, name='post_detail'),
]
