from django.db import models
from ckeditor.fields import RichTextField  # CKEditor используется для RichTextField
from hospital_departments.models import Department


class Vacancy(models.Model):
    specialty = models.CharField(max_length=255, verbose_name="Специальность")
    salary = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Зарплата"
    )
    information = RichTextField(verbose_name="Информация")
    contact_info = RichTextField(verbose_name="Контактная информация")
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="vacancies",
        verbose_name="Отделение больницы",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return f"{self.specialty} - {self.department.name}"