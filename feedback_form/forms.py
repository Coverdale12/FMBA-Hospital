# feedback_form/forms.py
from django import forms
from .models import Feedback
from captcha.fields import CaptchaField

class FeedbackForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Feedback
        fields = ['full_name', 'email', 'subject', 'message', 'image',]
    
    def clean(self):
        cleaned_data = super().clean()
        full_name = cleaned_data.get("full_name")
        email = cleaned_data.get("email")
        subject = cleaned_data.get("subject")
        message = cleaned_data.get("message")

        if not all([full_name, email, subject, message]):
            raise forms.ValidationError("Всё обязательные поля должны быть заполнены.")