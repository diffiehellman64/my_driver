from django.urls import re_path
from driver.views import VehicleViewSet

urlpatterns = [
    re_path(r"^rv/", VehicleViewSet, name='VehicleViewSet'),
]