from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Employee serializer.
    """

    class Meta:
        model = Employee
        fields = ("name", "email", "department")


emp1 = {
    "name": "Felipe Morais",
    "email": "felipe.morais@igs-software.com.br",
    "department": "Tester",
}
emp2 = {
    "name": "Tatiane Laura",
    "email": "tatiane.laura@igs-software.com.br",
    "department": "Developer",
}
emp3 = {
    "name": "Mauricio Alegretti",
    "email": "mauricio.alegretti@igs-software.com.br",
    "department": "RH",
}

# Intantiate the serializer
emp1_serializer = EmployeeSerializer(data=emp1)
emp2_serializer = EmployeeSerializer(data=emp2)
emp3_serializer = EmployeeSerializer(data=emp3)

# Check if the serializer is valid
emp1_serializer.is_valid()
emp2_serializer.is_valid()
emp3_serializer.is_valid()

# Save the serializer
emp1_serializer.save()
emp2_serializer.save()
emp3_serializer.save()
