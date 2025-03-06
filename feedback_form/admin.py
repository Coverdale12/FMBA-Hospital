
from django.contrib import admin
from .models import Feedback
from django.utils.safestring import mark_safe



@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'created_at', 'image')  # Параметры, отображаемые в списке
    search_fields = ('full_name', 'email', 'message')    # Поля для поиска
    list_filter = ('created_at',)    
                   # Фильтр по дате создания
def image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="width: 100px; height: auto;" />')
        return 'Нет изображения'
image.short_description = 'Изображение'  # Переименование заголовка колонки
