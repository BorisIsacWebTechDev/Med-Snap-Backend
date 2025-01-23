from django.contrib import admin
# Register your models here.
from .models import Customers



class CusCustomersAdmin(admin.ModelAdmin):
    fields = ['full_name', 'slug']

admin.site.register(Customers)
