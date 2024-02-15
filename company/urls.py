from django.urls import path
from rest_framework import permissions
from .views import (
    CompanyApiView,
    DetailCompanyView,
)


urlpatterns = [
    path('companylist', CompanyApiView.as_view(), name="company-list"),
    path('companydetail/<int:id>/', DetailCompanyView.as_view(), name="company-detail")
]
