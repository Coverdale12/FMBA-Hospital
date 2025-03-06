
from django.urls import path
from .views import news_list, news_info

urlpatterns = [
    path('', news_list, name='news_list'),
    path('<int:news_id>/', news_info, name='news_info'),

]