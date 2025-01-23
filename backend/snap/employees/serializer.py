from rest_framework import serializers

from .models import AbstractClinicalEmployee


class AbstractClinicalEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractClinicalEmployee
        fields = ('id','first_name', 'last_name', 'contact_number', 'employee_type')