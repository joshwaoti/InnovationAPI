from django.urls import path
from .views import LocationListView, LocationDetailView

urlpatterns = [
    path('list/', LocationListView.as_view()),
    path('locationdetail/<int:pk>/', LocationDetailView.as_view()),
]
