from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_view, {'slug': 'prevention'}, name='prevention'),
    path('<slug:slug>/', views.page_view, name='prevention_page'),
]