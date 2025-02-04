from django.contrib.auth import views as auth_views
from django.urls import path, include, reverse_lazy


from .views import EmployeesAPIList

from .views import *

app_name='employee'

urlpatterns = [
    path('employees_list', EmployeesAPIList.as_view()),
    path("login/", LoginView.as_view(),name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"), #my own registration method
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),

    #PASSWORD RESET

    path('password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name="employees/password_reset_form.html",
            email_template_name="employees/password_reset_email.html",
            success_url=reverse_lazy("employee:password_reset_done")
        ),
        name='password_reset'
    ),

    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name="employees/password_reset_done.html"
        ),
        name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="employees/password_reset_confirm.html",
        success_url=reverse_lazy("employee:password_reset_complete")
        ),
         name='password_reset_confirm'
    ),

    path('password-reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name="employees/password_reset_complete.html"
        ),
        name='password_reset_complete'),
]