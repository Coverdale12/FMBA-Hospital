from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from django.views.generic import TemplateView
from flask import request



# Create your views here.

def error(request):
    return render(request, 'main/error.html')

def about(requests):
    return HttpResponse('About page \ Страничка о нас')

def hospital_departments(request):
    return render(request, 'hospital_departments/hospital_departments.html')

def feedbacks_navigate(request):
    return render(request, 'main/feedback_navigate.html')

def aboutus(request):
    return render(request, 'main/aboutus.html')

from News.models import News  # Импортируйте модель новостей
from comments.models import Comment
from .models import MainDoctorContent

def index(request):
    news_list = News.objects.all()
    comments = Comment.objects.all().order_by('-created_at')
    try:
        main_doctor_content = MainDoctorContent.objects.first()
    except MainDoctorContent.DoesNotExist:
        main_doctor_content = None
    context = {
        'news_list': news_list,
        'comments': comments,
        'main_doctor_content': main_doctor_content,
    }
    return render(request, 'main/index.html', context)

from .models import AboutUsPage

def aboutus(request):
    page = AboutUsPage.objects.first()
    context = {
        'page': page
    }
    return render(request, 'main/aboutus.html', context)












