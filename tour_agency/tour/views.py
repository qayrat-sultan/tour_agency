# from django.shortcuts import render
from django.views.generic import ListView, DetailView

from tour_agency.tour.models import Tour


class TourListView(ListView):
    """Список фильмов"""
    model = Tour
    queryset = Tour.objects.filter()
    paginate_by = 1


class TourDetailView(DetailView):
    model = Tour
