from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import EmailVerification, User
from products.models import Basket
from django.contrib.auth.decorators import login_required


class EmailVerificationView(TemplateView):
    template_name = 'users/email_verification.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "StoreShop - Подтверждение электронной почты"
        return context

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, code=code)
        if email_verification.exists() and not email_verification.first().is_expired():
            user.is_verify_email = True
            user.save()
            return super().get(request, *args, **kwargs)
        else:
            return redirect('index')


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active and user.is_verify_email:
                auth.login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # subject = 'Ваш аккаунт создан'
            # message = username + "! Добро пожаловать в Store!"
            # try:
            #     send_mail(
            #         subject,
            #         message,
            #         settings.EMAIL_HOST_USER,
            #         [email]
            #     )
            # except BadHeaderError:
            #     return HttpResponse("Обнаружен неверный заголовок")

            form.save()
            messages.success(request, "Подтвердите регистрацию по почте")
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'users/register.html', context)


@login_required(login_url='/users/login/')
def profile(request):
    user = request.user
    if request.method == "POST":
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)

    baskets = Basket.objects.filter(user=user)
    total_quantity = sum(basket.quantity for basket in baskets)  # [3, 2]
    total_sum = sum(basket.sum() for basket in baskets)  # [3597.00, 5878.00]

    context = {
        'title': "Store - Профиль",
        'form': form,
        'baskets': Basket.objects.filter(user=user),
        'total_quantity': total_quantity,
        'total_sum': total_sum,
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return redirect('index')
