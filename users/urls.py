from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('signup/', signup_view, name="signup"),
    path('appoinment/', appionment, name="appoinment"),
    path('confirmation/', confirmation, name="confirmation"),
]