from django.contrib import admin

# Register your models here.
# News/admin.py

from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'image', 'created_at')
    list_editable = ('title', 'content', 'image')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)