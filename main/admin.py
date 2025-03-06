from django.contrib import admin
from .models import MainDoctorContent

@admin.register(MainDoctorContent)
class MainDoctorContentAdmin(admin.ModelAdmin):
    list_display = ("title",)

from .models import AboutUsPage
from .models import UploadedFile

class UploadedFileInline(admin.TabularInline):
    model = UploadedFile
    extra = 1

@admin.register(AboutUsPage)
class AboutUsPageAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [UploadedFileInline]





