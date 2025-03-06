   # hospital_departments/urls.py
from django.urls import path
from . import views

urlpatterns = [
       path('', views.hospital_departments, name='hospital_departments'),
       path('<str:department_type>/', views.department_list, name='department_list'),
       path('info/<int:department_id>/', views.department_info, name='department_info'),
   ]