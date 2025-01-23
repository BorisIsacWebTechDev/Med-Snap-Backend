from django.contrib import admin
from .models import Services

# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'scheduling_date', 'scheduling_time_start', 'dr_id', 'customer_id', 'scheduling_id']

admin.site.register(Services, ServicesAdmin)