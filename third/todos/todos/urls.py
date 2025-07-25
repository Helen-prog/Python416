"""
URL configuration for todos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth (регистрация и авторизация)
    path('signup/', views.signup_user, name='signupuser'),
    path('logout/', views.logout_user, name='logoutuser'),
    path('login/', views.login_user, name='loginuser'),

    # Todos (постановка задач)
    path('current/', views.current_todos, name="currenttodos"),
    path('', views.home, name="home"),
    path('create/', views.create_todo, name="createtodo"),
    path('todo/<int:todo_pk>/', views.view_todo, name="viewtodo"),
    path('todo/<int:todo_pk>/complete', views.complete_todo, name="completetodo"),
    path('completed/', views.completed_todos, name="completedtodos"),
    path('todo/<int:todo_pk>/delete', views.delete_todo, name="deletetodo"),
]
