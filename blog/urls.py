from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
    path('category/<slug:slug>/', views.category_article, name='category_article'),
    path('tag/<slug:slug>/', views.tag_article, name='tag_article'),
    path('articles/search', views.search, name='search'),
]