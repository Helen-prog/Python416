from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            print('Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print("Username or password is incorrect")

    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def profiles(request):
    prof = Profile.objects.all()
    context = {
        'profiles': prof
    }
    return render(request, 'users/index.html', context)


def user_profile(request, pk):
    prof = Profile.objects.get(id=pk)

    top_skills = prof.skill_set.exclude(description__exact="")
    other_skills = prof.skill_set.filter(description="")

    context = {
        'profile': prof,
        'top_skills': top_skills,
        'other_skills': other_skills,
    }

    return render(request, 'users/profile.html', context)
