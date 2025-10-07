from django.shortcuts import render


def first_page(request):
    return render(request, 'cms/index.html')
