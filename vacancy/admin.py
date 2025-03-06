from django.contrib import admin
from .models import Vacancy



@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("specialty", "salary", "department", "created_at")
    list_filter = ("department", "created_at")
    search_fields = ("specialty", "information")