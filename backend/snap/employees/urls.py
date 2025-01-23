from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from rest_framework.urls import app_name

from .views import EmployeesAPIList

from .views import *

app_name='employee'

urlpatterns = [
    path('employees_list', EmployeesAPIList.as_view()),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]