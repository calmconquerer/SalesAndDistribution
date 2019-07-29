from django.db import models
import datetime


class EmployeeDetails(models.Model):
    employee_id = models.CharField(max_length=100, null=True)
    full_name = models.CharField(max_length=30, blank=False)
    date_of_birth = models.DateField(default=datetime.date)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=13, null=True)
    cnic = models.CharField(max_length=13, blank=False)
    bank_details = models.TextField(max_length=1000)
    address = models.TextField(max_length=1000)
