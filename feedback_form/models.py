from django.db import models

# Create your models here.


class Feedback(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    email = models.EmailField(verbose_name="Почта")
    subject = models.CharField(max_length=255, verbose_name="Тема")
    message = models.TextField(verbose_name="Обращение")
    image = models.ImageField(upload_to='feedback_images/', blank=True, null=True, verbose_name="Изображение")  # Этот путь нужно будет настроить
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    class Meta:
        verbose_name = "обращение"
        verbose_name_plural = "Обращения"

    def __str__(self):
        return self.subject