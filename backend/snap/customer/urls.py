from django.urls import path, include
from .views import CusttomerViewSet
from rest_framework import routers


app_name="customers"

router = routers.DefaultRouter()
router.register(r'Customers', CusttomerViewSet)

urlpatterns = [
   path("custtomer_view_set/", CusttomerViewSet.as_view({'get': 'list', 'post': 'create'})),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]