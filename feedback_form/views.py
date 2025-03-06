# feedback_form/views.py
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def feedback_form_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feedback_form')  # Добавьте URL для успешного обращения
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback_form/feedback_form.html', {'form': form})

@login_required
def feedback_list_view(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    paginator = Paginator(feedbacks, 10)  # 10 обращений на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'feedback_form/feedback_list_admin.html', {'page_obj': page_obj})