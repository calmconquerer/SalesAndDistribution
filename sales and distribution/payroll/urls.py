from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.employee, name='employee'),
    path('employee/new/', views.employee_register, name='employee-register'),
    path('employee_salary/new/', views.new_employee_salary, name='new-employee-salary'),
    path('employee_salary', views.employee_salary, name='employee-salary'),
    path('employee/delete/<int:pk>', views.delete_employee, name='delete-employee'),
    path('employee_salary/edit/<int:pk>', views.edit_employee_salary, name='edit-employee-salary'),
    path('payroll_reports/', views.reports, name='payroll-reports'),
    path('employee_details/pdf/', views.employee_details_report, name='employee-details-report'),
    path('employee_salary/pdf/', views.employee_salary_report, name='salary-report'),
]
