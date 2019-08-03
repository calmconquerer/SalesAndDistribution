from django.shortcuts import render, redirect
from .models import EmployeeDetails, EmployeeHeader
from django.db import connection
from django.contrib import messages
import datetime, json
from transaction.models import Company_info
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from .utils import render_to_pdf


def employee_register(request):
    employee_register = EmployeeHeader.objects.all()

    cursor = connection.cursor()
    get_last_emp_id = cursor.execute('''select employee_id from payroll_employeeheader where employee_id LIKE '%EMP%'
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
        employee_details = EmployeeHeader(employee_id=get_last_emp_id , full_name=full_name, date_of_birth=date_of_birth, email=email, cnic=cnic,
                                           bank_details=bank_details, address=address, mobile=mobile_number)
        employee_details.save()
        return redirect('employee')
    return render(request, 'payroll/employee_register.html', {'employee_register': employee_register,
                                                              'emp_id': get_last_emp_id})


def employee(request):
    employee = EmployeeHeader.objects.all()
    return render(request, 'payroll/employee.html', {'employee': employee})


def delete_employee(request, pk):
    EmployeeHeader.objects.filter(id=pk).delete()
    messages.add_message(request, messages.SUCCESS, "Employee Deleted")
    return redirect('employee')


def employee_salary(request):
    cursor = connection.cursor()
    employee_salary_details = cursor.execute('''SELECT payroll_employeeheader.id, payroll_employeeheader.employee_id, payroll_employeeheader.full_name, payroll_employeedetails.join_date, payroll_employeedetails.salary From payroll_employeeheader, payroll_employeedetails
WHERE payroll_employeeheader.id = payroll_employeedetails.header_id_id''')
    employee_salary_details = employee_salary_details.fetchall()
    return render(request, 'payroll/employee_salary.html', {'employee_salary_details': employee_salary_details})


def new_employee_salary(request):
    all_employee = EmployeeHeader.objects.all()
    name = request.POST.get('select_name')
    if name:
        row = EmployeeHeader.objects.filter(id=name).first()
        row = row.employee_id
        return HttpResponse(json.dumps({'row': row}))
    if request.method == 'POST':
        join_date = request.POST.get('join_date', False)
        salary = request.POST.get('salary', False)
        full_name = request.POST.get('full_name')
        full_name = EmployeeHeader.objects.get(id=full_name)
        employee_detail = EmployeeDetails(header_id=full_name, salary=salary, join_date=join_date)
        employee_detail.save()
        return redirect('employee-salary')
    return render(request, 'payroll/new_employee_salary.html', {'all_employee': all_employee})


def edit_employee_salary(request, pk):
    employee_header = EmployeeHeader.objects.filter(id=pk).first()
    employee_detail = EmployeeDetails.objects.filter(header_id=pk).first()

    if request.method == 'POST':
        salary = request.POST.get('salary', False)

        employee_detail.salary = salary
        employee_detail.save()
        messages.add_message(request, messages.SUCCESS, "Salary Updated")
        return redirect('employee-salary')
    return render(request, 'payroll/edit_employee_salary.html', {'employee_header': employee_header,
                                                                 'employee_detail': employee_detail})


def reports(request):
    return render(request, 'payroll/payroll_reports.html')


def employee_details_report(request):
    company_info = Company_info.objects.all()
    employee_header = EmployeeHeader.objects.all()
    date_printed = datetime.date.today()

    pdf = render_to_pdf('payroll/employee_details_pdf.html', {'company_info': company_info,
                                                                 'employee_header': employee_header,
                                                                 'date_printed': date_printed})

    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "EmployeeDetail%s.pdf" % ("000")
        content = "inline; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return redirect("payroll-reports")


def employee_salary_report(request):
    cursor = connection.cursor()
    employee_salary_details = cursor.execute('''SELECT payroll_employeeheader.employee_id, payroll_employeeheader.full_name, payroll_employeedetails.salary From payroll_employeeheader, payroll_employeedetails
WHERE payroll_employeeheader.id = payroll_employeedetails.header_id_id''')
    company_info = Company_info.objects.all()
    pdf = render_to_pdf('payroll/employee_salary_pdf.html', {'company_info': company_info,
                                                             'employee_salary_details': employee_salary_details})

    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "EmployeeDetail%s.pdf" % ("000")
        content = "inline; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return redirect("payroll-reports")


















