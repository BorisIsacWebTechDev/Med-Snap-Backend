from django.contrib import admin
from .models import CustomUser, SingleUser,ReceptionsClinicalEmployee, HospitalUser


class SingleUserAdmin(admin.ModelAdmin):
    exclude = ['username']
    list_display = ['employee_type', 'first_name', 'last_name', 'is_staff']

class ReceptionsClinicalEmployeeAdmin(admin.ModelAdmin):
    exclude = ['username']
    list_display = ['employee_type', 'first_name', 'last_name']

class HospitalUSerAdmin(admin.ModelAdmin):
    list_display = ['name', 'tax_id', 'clinical_type', 'email', 'number_of_staff']

# Register your models here.
admin.site.register(SingleUser, SingleUserAdmin)
admin.site.register(ReceptionsClinicalEmployee, ReceptionsClinicalEmployeeAdmin)
admin.site.register(HospitalUser, HospitalUSerAdmin)


