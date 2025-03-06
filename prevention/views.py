from django.shortcuts import render, get_object_or_404
from .models import Page


def page_view(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'prevention/prevention.html', {'page': page})