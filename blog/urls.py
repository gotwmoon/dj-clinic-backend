from django.urls import path
from .views import *

urlpatterns = [
    path('', blog_view, name='blog-view'),
    path('<int:pid>/', blog_single, name='blog-single'),
]