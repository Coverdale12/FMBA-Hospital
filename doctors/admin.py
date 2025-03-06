from django.contrib import admin
from .models import Doctor, Schedule

class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 1

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id','last_name', 'first_name', 'middle_name', 'specialty', 'description', 'photo']
    list_editable = ('last_name', 'first_name', 'middle_name', 'specialty', 'description', 'photo')
    
    inlines = [ScheduleInline]
    

admin.site.register(Doctor, DoctorAdmin)

admin.site.site_header = "Администрация сайта"
admin.site.index_title = "Админ-панель"