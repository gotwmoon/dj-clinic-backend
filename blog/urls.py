from django.urls import path
from .views import *

urlpatterns = [
    path('', blog_view, name='blog-view'),
    path('<int:pid>/', blog_single, name='blog-single'),
    path('category/<str:cat_name>/', blog_view, name='blog-category'),
    path('tag/<str:tag_name>/', blog_view, name='blog-tag'),
]