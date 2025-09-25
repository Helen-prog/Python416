from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('verify/<str:email>/<uuid:code>/', views.EmailVerificationView.as_view(), name='email_verification'),

    path('reset-password/', auth_views.PasswordResetView.as_view(template_name="users/reset_password.html"), name='reset-password'),
    #
    # пользователь вводит электронный адрес для сброса пароля
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="users/reset_password_sent.html"), name='password_reset_done'),
    # сообщение отправленное по электронной почте
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/reset.html"), name='password_reset_confirm'),
    # электронное письмо со ссылкой и инструкциями для сброса пароля
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/reset_password_complete.html"), name='password_reset_complete'),
    # сообщение об успешном сбросе пароля
]
