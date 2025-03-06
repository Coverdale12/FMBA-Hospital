# feedback_form/urls.py
from django.urls import path
from .views import feedback_form_view, feedback_list_view

urlpatterns = [
    path('form/', feedback_form_view, name='feedback_form'),
    path('list/', feedback_list_view, name='feedback_list'),
]