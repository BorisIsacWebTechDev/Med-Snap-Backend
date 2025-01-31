from django.shortcuts import render
from .serializers import *
from .models import Customers
from rest_framework import permissions, viewsets

class CusttomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customers to be viewed or edited.
    """
    queryset = Customers.objects.all().order_by('full_name')
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]