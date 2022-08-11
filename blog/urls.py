from django.urls import path
from .views import *

from django.urls import path
from .feeds import LatestEntriesFeed

urlpatterns = [
    path('', blog_view, name='blog-view'),
    path('<int:pid>/', blog_single, name='blog-single'),
    path('category/<str:cat_name>/', blog_view, name='blog-category'),
    path('tag/<str:tag_name>/', blog_view, name='blog-tag'),
    path('search/', blog_search, name='search'),
     path('rss/feed/', LatestEntriesFeed()),
]