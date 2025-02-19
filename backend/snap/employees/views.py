from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from  .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic.edit import CreateView


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
            return redirect('main:index')

        return render(request, 'employees_form_template.html', context)


class LogoutView(View):
    def get(self, request):
        # Log out the user
        logout(request)
        # Redirect to the login page or any other page
        return redirect('main:index')  # Replace 'login' with the name of your login URL pattern


class RegisterSingleView(View):
    '''
    registration single class
    '''
    def get(self, requests):
        '''
        get method for printing form
        :param requests:
        :return rendered page with a form for registration:
        '''
        form = RegisterSingleForm()
        if form:
            context = {
                'title': 'Registration',
                'title_form': 'Registration new Small Office',
                'form': form,
                'button_submit': 'Register New small office'
            }
            return render(requests, 'employees_form_template.html', context=context)


    def post(self, request):
        form = RegisterSingleForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_dr_office = DrClinicalEmployee(
                email=cd['email'],
                password=make_password(cd['password1']),
                first_name=cd['first_name'],
                last_name=cd['last_name'],
                contact_number=cd['contact_number'],
                gender=cd['gender'],
                medical_order_id = cd['medical_order_id'],
                specialty_type = cd['specialty_type'],
                is_staff=True,
                is_superuser = True,
            )
            new_dr_office.save()
            return redirect(reverse("employees:login"))
        context = {
            "error_msg": "something is wrong in your registration", 
            'title': 'Registration',
            'title_form': 'Registration new Small Office',
            'form': form,
            'button_submit': 'Register New small Office'
        }
        print(context)
        return render(request, 'employees_form_template.html', context)


class RegisterHospitalView(View):
    '''
    registration hospital class
    '''
    def get(self, requests):
        '''
        get method for printing form
        :param requests:
        :return rendered page with a form for registration:
        '''
        form = RegisterHospitalForm()
        addicional_form = RegisterSingleForm()
        
        if form:
            context = {
                'title': 'Registration',
                'title_form': 'Registration new hospital',
                'form': form,
                'addicional_form': addicional_form,
                'button_submit': 'Register New hospital',
                'head_title' : 'Head physician\'s data'.upper()
            }
            return render(requests, 'employees_form_template.html', context=context)


    def post(self, request):
        form = RegisterHospitalForm(data=request.POST)
        addicional_form = RegisterSingleForm(data=request.POST)
        if form.is_valid() and addicional_form.is_valid():
            cd = addicional_form.cleaned_data

            new_dr, created = DrClinicalEmployee.objects.get_or_create(
                email=cd['email'],
                defaults={
                    'password': make_password(cd['password1']),
                    'first_name': cd['first_name'],
                    'last_name': cd['last_name'],
                    'contact_number': cd['contact_number'],
                    'gender': cd['gender'],
                    'medical_order_id': cd['medical_order_id'],
                    'specialty_type': cd['specialty_type'],
                    'is_staff': True,
                    'is_superuser': True,
                }
            )


            if not created:
                 context = {                     
                    "error_msg": "something is wrong in your registration",
                    'title': 'Registration',
                    'title_form': 'Registration new hospital',
                    'form': form,
                    'addicional_form': addicional_form,
                    'button_submit': 'Register New hospital',
                    'head_title' : 'Head physician\'s data'.upper(),
                    'error_msg': 'A doctor with this email already exists.'

                 }
                 return render(request, 'employees_form_template.html', context)
            
            cd = form.cleaned_data
            new_hospital = HospitalUser.objects.create(
                clinical_name=cd['clinical_name'],
                clinical_email = cd['clinical_email'],
                clinical_phone = cd['clinical_phone'],
                tax_id=cd['tax_id'],
                clinical_type=cd['clinical_type'],
                country=cd['country'],
                city=cd['city'],
                address=cd['address'],
                zip_code=cd['zip_code'],
                num_staff=cd['num_staff'],
                head_physician = new_dr
            )
            new_hospital.save()
            
            return redirect(reverse("employees:login"))
        context = {
            "error_msg": "something is wrong in your registration",
            'title': 'Registration',
            'title_form': 'Registration new hospital',
            'form': form,
            'addicional_form': addicional_form,
            'button_submit': 'Register New hospital',
            'head_title' : 'Head physician\'s data'.upper(),
            'error_msg': 'A doctor with this email already exists.'
              }
        print(context)
        return render(request, 'employees_form_template.html', context)
