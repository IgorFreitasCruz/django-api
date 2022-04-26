from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Employee serializer.
    """

    class Meta:
        model = Employee
        fields = ("name", "email", "department")
