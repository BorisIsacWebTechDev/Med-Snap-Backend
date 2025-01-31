from django.contrib.auth import views as auth_view
from django.urls import path, include, reverse_lazy
from rest_framework.urls import app_name


from .views import EmployeesAPIList

from .views import *

app_name='employee'

urlpatterns = [
    path('employees_list', 
        EmployeesAPIList.as_view()
        ),
    
    path("login/", 
        LoginView.as_view(), 
        name="login"
        ),
    
    path("logout/", 
        LogoutView.as_view(), 
        name="logout"
        ),
    
    path("register/", 
        RegisterView.as_view(), 
        name="register"
        ), #my own registrathio method
    
    path('password-change/', 
        auth_view.PasswordChangeView.as_view(
            success_url=reverse_lazy('employee:password_change_done')
        ), 
        name="password_change"
    ),
    
    path('password-changed/done',
        auth_view.PasswordChangeDoneView.as_view(),
        name = 'password_change_done'
    ),

    path('password-reset/',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
 
    path('password-reset/complete/',
        auth_view.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
]