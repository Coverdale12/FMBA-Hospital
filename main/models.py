from ckeditor.fields import RichTextField
from django.db import models


class MainDoctorContent(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок (Не отображается")
    content = RichTextField(verbose_name="Информация")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Информация на главной странице"
        verbose_name_plural = "Информация на главной странице"

class AboutUsPage(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок (Не отображается)")
    content = RichTextField(verbose_name="Информация")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страница 'О нас'"
        verbose_name_plural = "Страница 'О нас'"

class UploadedFile(models.Model):
    page = models.ForeignKey(
        AboutUsPage, on_delete=models.CASCADE,
        related_name="files", verbose_name="Страница"
    )
    file = models.FileField(upload_to="aboutus_files/", verbose_name="Файл")
    display_name = models.CharField(
        max_length=200, verbose_name="Имя файла на сайте", blank=True
    )

    def __str__(self):
        return self.display_name or self.file.name

    class Meta:
        verbose_name = "Файл для страницы 'О нас'"
        verbose_name_plural = "Файлы для страницы 'О нас'"

