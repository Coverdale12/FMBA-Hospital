# comments/urls.py
from django.urls import path
from .views import comment_list, add_comment, edit_comment, delete_comment, comment_list_json

urlpatterns = [
    path('', comment_list, name='comment_list'),
    path('get/', comment_list_json, name='comment_list_json'),
    path('add/', add_comment, name='add_comment'),
    path('edit/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('delete/<int:comment_id>/', delete_comment, name='delete_comment'),
]