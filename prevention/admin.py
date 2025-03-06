from django.contrib import admin
from .models import Page, UploadedFile


class UploadedFileInline(admin.TabularInline):
    model = UploadedFile
    extra = 1
    fields = ('file', 'display_name',)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'updated_at')
    list_filter = ('slug',)
    search_fields = ('title', 'content')
    ordering = ('slug',)
    inlines = [UploadedFileInline]