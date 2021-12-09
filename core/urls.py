from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('categories/<slug:slug>/', views.by_category, name='by_category'),
    path('tags/<slug:slug>/', views.by_tag, name='by_tag'),
    path('posts/<slug:slug>/', views.article_page, name='post_detail'),
    path('search/', views.search, name='search'),
]
