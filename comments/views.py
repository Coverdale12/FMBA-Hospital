from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .utils import filter_comment

def comment_list_json(request):
    comments = Comment.objects.all().order_by('-created_at')
    
    # Формируем список словарей для каждого комментария
    comments_data = [
        {
            'id': comment.id,
            'name': comment.user.username,
            'content': comment.content,
            'datatime': comment.created_at.strftime('%Y-%m-%d')  # Форматируем дату
        }
        for comment in comments
    ]
    return JsonResponse({'message': comments_data})

# @login_required
def comments_view(request):
    comments = Comment.objects.all()
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            # Создание временного объекта комментария для фильтрации
            temp_comment = Comment(content=content, user=request.user)  # Замена на правильное поле пользователя
            if filter_comment(temp_comment):
                Comment.objects.create(user=request.user, content=content)
                return redirect('comments')
            else:
            
                error_message = "Ваш комментарий содержит неподобающие слова."
                return render(request, 'comments/comments.html', {'comments': comments, 'error_message': error_message})

    return render(request, 'comments/comments.html', {'comments': comments})

@login_required
def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user != comment.user and not request.user.is_superuser:
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('comments')
    
 
    
    return render(request, 'comments/edit_comment.html', {'comment': comment})

@login_required
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.user or request.user.is_superuser:
        comment.delete()
    return redirect('comments')