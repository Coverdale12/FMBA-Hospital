from django.db import models
from ckeditor.fields import RichTextField


class UslugiPage(models.Model):
    PAGE_CHOICES = [
        ('uslugi', 'Услуги'),
        ('uslugi_oms', 'Услуги по ОМС'),
        ('uslugi_paid', 'Платные услуги'),
    ]

    slug = models.CharField(
        max_length=50,
        unique=True,
        choices=PAGE_CHOICES,
        verbose_name="Страница"
    )
    title = models.CharField(max_length=200, verbose_name="Заголовок страницы")
    content = RichTextField(verbose_name="Контент", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    def __str__(self):
        return dict(self.PAGE_CHOICES).get(self.slug, self.slug)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"


class UploadedFile(models.Model):
    page = models.ForeignKey(
        UslugiPage,
        on_delete=models.CASCADE,
        related_name="files",
        verbose_name="Страница"
    )
    file = models.FileField(upload_to="uslugi_files/", verbose_name="Файл")
    display_name = models.CharField(
        max_length=200,
        verbose_name="Имя файла на сайте",
        blank=True
    )

    def __str__(self):
        return self.display_name or self.file.name

    class Meta:
        verbose_name = "Файл для страницы"
        verbose_name_plural = "Файлы для страниц"