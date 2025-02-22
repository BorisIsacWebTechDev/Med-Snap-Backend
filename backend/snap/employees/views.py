from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.hashers import make_password

from .serializer import AbstractClinicalEmployeeSerializer
from  .models import *

from .forms import *



from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic.edit import CreateView


class EmployeesAPIList(generics.ListAPIView):
    queryset = AbstractClinicalEmployee.objects.all()
    print(queryset)
    serializer_class = AbstractClinicalEmployeeSerializer


from .forms import RegisterForm

class LoginView(View):  # Use a distinct name for the view
    def get(self, request):
        form = LoginForm()  # Instantiate the form
        context = {
            'form': form,
            'title': 'Login',
            'title_form': 'Login Employ',
            'button_submit': 'Login',
            'is_get_method': request.method == 'GET'
        }
        return render(request, 'employees_form_template.html', context)

    def post(self, request):
        form = LoginForm(data=request.POST)

        context = {
            'form': form,
            'title': 'Login',
            'title_form': 'Login Employ',
            'button_submit': 'Login',
            'is_get_method': request.method == 'GET'
        }

        if form.is_valid():
            cd = form.cleaned_data
            email = cd['username']
            psw = cd['password']
            employee = authenticate(request,email=email, password=psw)
            if employee:
                login(request, employee)
            return redirect('main:index')  # Replace with your success URL

        return render(request, 'employees_form_template.html', context)


class LogoutView(View):
    def get(self, request):
        # Log out the user
        logout(request)
        # Redirect to the login page or any other page
        return redirect('main:index')  # Replace 'login' with the name of your login URL pattern


class RegisterView(View):
    '''
    registration class
    '''

    def get(self, requests):
        '''
        get method for printing form
        :param requests:
        :return rendered page with a form for registration:
        '''
        form = RegisterForm()
        if form:
            context = {
                'title': 'Registration',
                'title_form': 'Registration new employee',
                'form': form,
                'button_submit': 'Register'
            }
            return render(requests, 'employees_form_template.html', context=context)


    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['employee_type'] == AbstractClinicalEmployee.EmployeeType.DOCTOR:
                print("Should be saved on dr table")
                new_dr_employee = DRClinicalEmployee(
                    email=cd['email'],
                    password=make_password(cd['password1']),
                    first_name=cd['first_name'],
                    last_name=cd['last_name'],
                    contact_number=cd['contact_number'],
                    employee_type=cd['employee_type'],
                    gender_employee=cd['gender_employee'],
                    is_staff=True
                )
                new_dr_employee.save()
            elif cd['employee_type'] == AbstractClinicalEmployee.EmployeeType.RECEPTION:
                print("Should be saved on receptions")
                new_reception_employee = ReceptionsClinicalEmployee(
                    email=cd['email'],
                    password=make_password(cd['password1']),
                    first_name=cd['first_name'],
                    last_name=cd['last_name'],
                    contact_number=cd['contact_number'],
                    employee_type=cd['employee_type'],
                    gender_employee=cd['gender_employee'],
                    is_staff=True
                )
                new_reception_employee.save()
            else:
                new_abstract_employee = AbstractClinicalEmployee(
                    email=cd['email'],
                    password=make_password(cd['password1']),
                    first_name=cd['first_name'],
                    last_name=cd['last_name'],
                    contact_number=cd['contact_number'],
                    employee_type=cd['employee_type'],
                    gender_employee=cd['gender_employee'],
                    is_staff=True
                )
                new_abstract_employee.save()
            return redirect(reverse("employees:login"))
        context = {"error_msg": "something is wrong in your registration" }
        print(context)
        return render(request, 'employees_form_template.html', context)



