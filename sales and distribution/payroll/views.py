from django.shortcuts import render
from .models import EmployeeDetails
from django.db import connection
import datetime
from django.http import JsonResponse, HttpResponse


def employee_register(request):
    employee_register = EmployeeDetails.objects.all()

    cursor = connection.cursor()
    get_last_emp_id = cursor.execute('''select employee_id from payroll_employeedetails where employee_id LIKE '%EMP%'
                                            order by employee_id DESC LIMIT 1''')
    get_last_emp_id = get_last_emp_id.fetchall()

    if get_last_emp_id:
        get_last_emp_id = get_last_emp_id[0][0]
        get_last_emp_id = get_last_emp_id[3:]
        serial = str((int(get_last_emp_id) + 1))
        get_last_emp_id ='EMP' + serial
    else:
        get_last_emp_id = 'EMP1'
    if request.method == 'POST':
        full_name = request.POST.get('full_name', False)
        date_of_birth = request.POST.get('date_of_birth', False)
        mobile_number = request.POST.get('mobile_number', False)
        email = request.POST.get('email', False)
        cnic = request.POST.get('cnic', False)
        bank_details = request.POST.get('bank_details', False)
        address = request.POST.get('address', False)
        employee_details = EmployeeDetails(employee_id=get_last_emp_id , full_name=full_name, date_of_birth=date_of_birth, email=email, cnic=cnic,
                                           bank_details=bank_details, address=address, mobile=mobile_number)
        employee_details.save()
        return JsonResponse({"result": "success"})
    return render(request, 'payroll/employee_register.html', {'employee_register': employee_register,
                                                              'emp_id': get_last_emp_id})
