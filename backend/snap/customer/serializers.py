from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = ['full_name', 'tel', 'email', 'nif', 'sns', 'address']
