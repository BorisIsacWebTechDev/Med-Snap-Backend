from django.contrib import admin
from .models import *


class BasicCustomEmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'is_staff']


class DrClinicalEmployeeAdmin(admin.ModelAdmin):
    exclude = ['username']
    list_display = ['first_name', 'last_name', 'is_staff']

class ReceptionsClinicalEmployeeAdmin(admin.ModelAdmin):
    exclude = ['username']
    list_display = ['first_name', 'last_name']

class HospitalUSerAdmin(admin.ModelAdmin):
    exclude = ['username', 'email', 'contact_number', 'first_name', 'last_name','gender', 'role', 'password1', "password2"]
    
# Register your models here.
admin.site.register(BasicCustomEmployee, BasicCustomEmployeeAdmin)
admin.site.register(DrClinicalEmployee, DrClinicalEmployeeAdmin)
admin.site.register(ReceptionsClinicalEmployee, ReceptionsClinicalEmployeeAdmin)
admin.site.register(HospitalUser, HospitalUSerAdmin)


