from django.db import models
from ckeditor.fields import RichTextField
 
# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)  # Изменено
    created_at = models.DateTimeField(auto_now_add=True)
    verbose_name = 'Мое Приложение'

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title