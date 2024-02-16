from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Company
from .serializers import CompanySerializer



class CompanyApiView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def  get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DetailCompanyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)



# class CompanyApiView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     # list al
#     def get(self, request, *args, **kwargs):
#         companies = Company.objects.all()
#         serializer = CompanySerializer(companies, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     # Create
#     def post(self, request, *args, **kwargs):
        
#         data = {
#             "name": request.data.get('name'),
#             "owner": request.data.get("owner"),
#             "about": request.data.get("about")
#         }
#         serializer = CompanySerializer(data=data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class DetailCompanyView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get_object(self, id):

#         try:
#             return Company.objects.get(id=id)
#         except Company.DoesNotExist:
#             return None
        
#     def get(self, request, id, *args, **kwargs):
#         company = self.get_object(id)
#         if not company:
#             return Response(status=status.HTTP_404_NOT_FOUND)
            
#         serializer = CompanySerializer(company, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     # update
#     def put(self, request, id, *args, **kwargs):
#         company = self.get_object(id)
#         if not company:
#             return Response(status=status.HTTP_404_NOT_FOND)
        
#         data = {
#             "name": request.data.get('name'),
#             "owner": request.data.get("owner"),
#             "about": request.data.get("about")
#         }
        
#         serializer = CompanySerializer(company, data=data, partial=True, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

#     #  delete
#     def delete(self, request, id, *args, **kwargs):
#         company = self.get_object(id)
#         if not company:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         company.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)