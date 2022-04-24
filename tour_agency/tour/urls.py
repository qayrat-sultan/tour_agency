from django.urls import path

from tour_agency.tour.views import TourListView, TourDetailView

app_name = "tour"

urlpatterns = [
    path('', TourListView.as_view(), name='list'),
    path('<int:pk>/', TourDetailView.as_view(), name='detail'),
]
