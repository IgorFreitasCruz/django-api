from django.urls import include, path
from rest_framework import routers

from .views import EmployeeViewSet

router = routers.DefaultRouter()
router.register(r"employee", EmployeeViewSet, basename="employees")

urlpatterns = [
    path("", include(router.urls), name="index"),
    
]
