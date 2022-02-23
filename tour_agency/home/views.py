from django.shortcuts import render
from django.views.generic import ListView

from tour_agency.home.models import Tour


class MoviesView(ListView):
    """Список фильмов"""
    model = Tour
    queryset = Tour.objects.filter(draft=False)
    paginate_by = 1
