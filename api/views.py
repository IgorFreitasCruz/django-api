from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Employee
from api.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    """

    def get_serializer_class(self):
        return EmployeeSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        queryset = Employee.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(queryset, pk=pk)
        return obj

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Employee.objects.all()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializer(obj)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        obj = self.get_object()
        serializer = self.get_serializer(
            obj,
            data=request.data,
            partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, pk=None):
        obj = self.get_object()
        obj.delete()
        return Response(status=204)


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

# Checking the database before creating new employees
get_list = EmployeeViewSet().list(None)
if not len(get_list.data):

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
