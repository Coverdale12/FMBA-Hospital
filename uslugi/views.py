from django.shortcuts import render, get_object_or_404
from .models import UslugiPage


def page_view(request, slug):
    page = get_object_or_404(UslugiPage, slug=slug)
    return render(request, 'uslugi/uslugi.html', {'page': page})