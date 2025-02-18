from rest_framework import serializers

from .models import SingleUser


class SingleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleUser
        fields = ('id','first_name', 'last_name', 'contact_number', 'employee_type')