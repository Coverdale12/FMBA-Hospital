from django.shortcuts import render, get_object_or_404
from .models import Vacancy, Department


def vacancy_list(request):
    # Получаем параметры из GET-запроса
    department_type = request.GET.get('department_type', '')  # Тип отделения ("children" или "adult")
    department_id = request.GET.get('department', '')  # ID конкретного отделения

    # Фильтруем отделения и вакансии
    all_departments = Department.objects.all()  # Полный список отделений
    vacancies = Vacancy.objects.all()  # Полный список вакансий

    # Фильтр по типу отделения ("children" или "adult")
    if department_type == 'children':
        filtered_departments = all_departments.filter(department_type='children')  # Фильтруем отделения
        vacancies = vacancies.filter(department__department_type='children')  # Фильтруем вакансии
    elif department_type == 'adult':
        filtered_departments = all_departments.filter(department_type='adult')  # Фильтруем отделения
        vacancies = vacancies.filter(department__department_type='adult')  # Фильтруем вакансии
    else:
        filtered_departments = all_departments  # Если тип отделения не выбран, показываем всё

    # Фильтр вакансий по конкретному отделению
    if department_id:  # Если выбирается конкретное отделение
        vacancies = vacancies.filter(department_id=department_id)

    # Контекст для передачи в шаблон
    context = {
        'departments': all_departments,  # Все отделения (для первой кнопки)
        'filtered_departments': filtered_departments,  # Отделения после фильтрации по type (для второй кнопки)
        'selected_department': int(department_id) if department_id else None,  # ID выбранного отделения
        'selected_department_type': department_type,  # Тип отделения ("children", "adult")
        'vacancies': vacancies,  # Отфильтрованные вакансии
    }
    return render(request, 'vacancy/vacancy_list.html', context)

def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    return render(request, "vacancy/vacancy_detail.html", {"vacancy": vacancy})