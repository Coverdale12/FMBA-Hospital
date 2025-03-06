from django.shortcuts import render, get_object_or_404
from .models import Department
from doctors.models import Doctor

def hospital_departments(request):
       return render(request, 'hospital_departments/hospital_departments.html')

def department_list(request, department_type):
       departments = Department.objects.filter(department_type=department_type)
       return render(request, 'hospital_departments/hospital_departments_list.html', {
           'departments': departments
       })

def department_info(request, department_id):
       department = get_object_or_404(Department, id=department_id)
       doctors = Doctor.objects.filter(department=department)
       title = f"{department.name}"
       return render(request, 'hospital_departments/hospital_departments_info.html', {
           'department': department,
           'doctors': doctors,
           'title': title,
       })


