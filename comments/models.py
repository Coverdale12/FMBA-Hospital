from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_from_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"
    
    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"
    


