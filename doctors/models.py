from django.db import models
from hospital_departments.models import Department
from ckeditor.fields import RichTextField

class Doctor(models.Model):
    





    first_name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=30, verbose_name="Отчество", blank=True, null=True)
    specialty = models.CharField(max_length=100, verbose_name="Специальность")
    description = RichTextField(verbose_name="Информация")
    photo = models.ImageField(upload_to='doctors_photos/', verbose_name="Фотография", null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_DEFAULT, default=1, verbose_name="Отделение")
    
    class Meta:
        verbose_name = "специалиста"
        verbose_name_plural = "Специалисты"




    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    
    

class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='schedules', verbose_name="Врач")
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Понедельник'),
        ('Tuesday', 'Вторник'),
        ('Wednesday', 'Среда'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятница'),
        ('Saturday', 'Суббота'),
        ('Sunday', 'Воскресенье'),
    ], verbose_name="День недели")
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")

    class Meta:
        unique_together = ('doctor', 'day_of_week')
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"

    def __str__(self):
        return f"{self.get_day_of_week_display()} - {self.start_time} to {self.end_time}"