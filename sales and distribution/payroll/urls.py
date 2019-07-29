from django.urls import path
from . import views

urlpatterns = [
    path('employee_register/', views.employee_register, name='employee-register')
]
