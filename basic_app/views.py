from django.shortcuts import render

# Create your views here.
from .import models, serializers
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class ListView(generics.ListCreateAPIView):
    queryset=models.ListApi.objects.all()
    serializer_class=serializers.ListApiSerializer
    
class RetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.ListApi.objects.all()
    serializer_class=serializers.ListApiSerializer
    
    
class TuriView(generics.ListCreateAPIView):
    queryset=models.TaomApi.objects.all()
    serializer_class=serializers.TaomApiSerializer
    
class TuriRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.TaomApi.objects.all()
    serializer_class=serializers.TaomApiSerializer