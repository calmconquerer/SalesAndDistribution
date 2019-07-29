from django.shortcuts import render
from .models import EmployeeDetails
from django.http import JsonResponse, HttpResponse


def employee_register(request):
    employee_register = EmployeeDetails.objects.all()
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        print(full_name)
        date_of_birth = request.POST.get('date_of_birth')
        print(date_of_birth)
        email = request.POST.get('email')
        cnic = request.POST.get('cnic')
        bank_details = request.POST.get('bank_details')
        address = request.POST.get('address', False)
        employee_details = EmployeeDetails(full_name=full_name, date_of_birth=date_of_birth, email=email, cnic=cnic,
                                           bank_details=bank_details, address=address)
        employee_details.save()
        return JsonResponse({"result": "success"})
    return render(request, 'payroll/employee_register.html', {'employee_register': employee_register})
