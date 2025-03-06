"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from main import views

from login.views import register, user_login
from comments.views import comments_view, edit_comment, delete_comment, comment_list_json
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace = 'main')),
    path('news/', include('News.urls')),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('comments/', comments_view, name='comments'),
    path('comments/edit/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('comments/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('comments/get', comment_list_json, name='comment_list_json'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('uslugi/', include('uslugi.urls')),
    path('doctors/', include('doctors.urls')),
    path('vacancies/', include('vacancy.urls')),  # Подключение урлов приложения vacancy
    path('departments/', include('hospital_departments.urls')),
    path('feedback/', include('feedback_form.urls')),
    path('captcha/', include('captcha.urls')),
    #path('services/', include('services.urls')),
    path('prevention/', include('prevention.urls')),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)