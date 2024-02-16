from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Location
from .serializers import LocationSerializer


class LocationListView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class  LocationDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)