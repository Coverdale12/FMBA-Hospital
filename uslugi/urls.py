from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_view, {'slug': 'uslugi'}, name='uslugi'),
    path('<slug:slug>/', views.page_view, name='uslugi_page'),
]