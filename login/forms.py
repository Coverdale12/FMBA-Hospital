from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    middle_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=True)
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'middle_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        """
        Переопределяем метод сохранения, чтобы автоматически задавать username = email.
        """
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Присваиваем email в качестве username
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user