from django.contrib import admin

from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "department" )
    search_fields = ("name",)
    list_filter = ("department",)

admin.site.register(Employee, EmployeeAdmin)
