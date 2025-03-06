   # hospital_departments/models.py
from django.db import models
from ckeditor.fields import RichTextField

class Department(models.Model):
       TYPE_CHOICES = [
           ('adult', 'Взрослая'),
           ('children', 'Детская')
       ]
       name = models.CharField(max_length=100, verbose_name="Название")
       location = models.CharField(max_length=255, verbose_name="Адрес")
       department_type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name="Отделение")
       description = RichTextField(verbose_name="Информация")

       class Meta:
        verbose_name = "отделение"
        verbose_name_plural = "Отделения больницы"
       

       def __str__(self):
           return self.name
       


