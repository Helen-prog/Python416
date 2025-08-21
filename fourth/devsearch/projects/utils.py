from .models import Project
from django.db.models import Q


def search_projects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    pr = Project.objects.filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query)
    )

    return pr, search_query
