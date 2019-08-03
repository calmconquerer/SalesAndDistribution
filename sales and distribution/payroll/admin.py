from django.contrib import admin
from .models import EmployeeDetails, EmployeeHeader

# Register your models here.

admin.site.register(EmployeeDetails)
admin.site.register(EmployeeHeader)