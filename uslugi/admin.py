from django.contrib import admin
from .models import UslugiPage, UploadedFile


class UploadedFileInline(admin.TabularInline):
    model = UploadedFile
    extra = 1
    fields = ('file', 'display_name',)


@admin.register(UslugiPage)
class UslugiPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'updated_at')
    list_filter = ('slug', )
    search_fields = ('title', 'content')
    ordering = ('slug', )
    inlines = [UploadedFileInline]