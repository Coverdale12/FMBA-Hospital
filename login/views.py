from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('login')  # Перенаправляем на страницу логина
    else:
        form = RegistrationForm()
    return render(request, 'login/register.html', {"form": form})
    

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']  # Здесь пользователь вводит email
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('comments')
        else:
            messages.error(request, "Неправильный email или пароль.")
    return render(request, 'login/login.html')