from django.contrib import admin
from .models import AbstractClinicalEmployee, DRClinicalEmployee,ReceptionsClinicalEmployee


class AbstractClinicalEmployeeAdmin(admin.ModelAdmin):
    exclude = ['username']
    list_display = ['employee_type', 'first_name', 'last_name', 'is_staff']

class DRClinicalEmployeeAdmin(admin.ModelAdmin):
    exclude = ['username']
    list_display = ['employee_type', 'first_name', 'last_name', 'medical_order_ID']

class ReceptionsClinicalEmployeeAdmin(admin.ModelAdmin):
    exclude = ['username']
    list_display = ['employee_type', 'first_name', 'last_name']
# Register your models here.
admin.site.register(AbstractClinicalEmployee, AbstractClinicalEmployeeAdmin)
admin.site.register(DRClinicalEmployee, DRClinicalEmployeeAdmin)
admin.site.register(ReceptionsClinicalEmployee, ReceptionsClinicalEmployeeAdmin)



