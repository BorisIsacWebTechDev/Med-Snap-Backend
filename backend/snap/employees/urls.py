from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from rest_framework.urls import app_name

from .views import *

app_name='employee'

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('signup_single/', RegisterSingleView.as_view(), name='register_single'),
    path('signup_hospital/', RegisterHospitalView.as_view(), name='register_hospital')

]