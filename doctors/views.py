from django.shortcuts import render, get_object_or_404
from .models import Doctor

def doctor_list(request):


    sort_by = request.GET.get('sort', 'department')  # Получаем параметр сортировки из URL, по умолчанию сортируем по имени

    # Проверяем, что переданный параметр сортировки допустим
    if sort_by not in ['specialty', 'department']:
        sort_by = 'department'  # Сортировка по умолчанию



    doctors = Doctor.objects.all().order_by(sort_by)
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})

def doctor_schedule(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    doctors = Doctor.objects.all()
    title = f"{doctor.first_name} { doctor.last_name } { doctor.middle_name}"
    return render(request, 'doctors/doctor_info.html', {'doctor': doctor, 'doctors': doctors, 'title': title})


