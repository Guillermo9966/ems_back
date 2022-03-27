from django.conf import UserSettingsHolder
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import filters
from django.shortcuts import render
import json
from django.http import Http404
from authentication.models import CustomUser


from monitoring.serializer import MonitoringSerializer, PlantSerializer, ReadingSerializer, SensorSerializer, ShiftSerializer, TypeMeditionSerializer
from .models import Company, Plant, Reading, Sensor, Shift, TypeMedition
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers

from rest_framework import generics
from rest_framework import status

class MonitoringManager(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = MonitoringSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user')
        queryset = Company.objects.filter(asigne_to=user)
        return queryset
    

class PlantList(generics.ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    def get_queryset(self):
      company = self.request.query_params.get('company')
      queryset = Plant.objects.filter(company=company) 
      return queryset 

class ShiftList(generics.ListAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

    def get_queryset(self):
       plant = self.request.query_params.get('plant')
       queryset = Shift.objects.filter(plant=plant)
       return queryset

class TypeMeditionList(generics.ListAPIView):
    queryset = TypeMedition.objects.all()
    serializer_class = TypeMeditionSerializer
    
    def get_queryset(self):
       plant = self.request.query_params.get('plant')
       queryset = TypeMedition.objects.filter(plant=plant)
       return queryset
     

class SensorList(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get_queryset(self):
      plant = self.request.query_params.get('plant')
      queryset = Sensor.objects.filter(plant=plant)
      return queryset  

class Readinglist(generics.ListAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer

    def get_queryset(self):
      sensor = self.request.query_params.get('sensor')
      queryset = Reading.objects.filter(sensor=sensor)  
      return queryset


# class MonitoringManager(APIView):
#     '''
#     list company 
#     '''
#     serializer_class = MonitoringSerializer
#     def get(self, request, format=None):
#         company = Company.objects.all()
#         serializer = MonitoringSerializer(company, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = MonitoringSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
# class PlantList(APIView):
#     serializer_class = PlantSerializer

#     def get(self, request, format=None):
#         plant = Plant.objects.all()
#         serializer = PlantSerializer(plant, many=True)
#         return Response(serializer.data)

# class ShiftList(APIView):
#     serializer_class = ShiftSerializer

#     def get(self, request, format=None):
#         shift = Shift.objects.all()
#         serializer = ShiftSerializer(shift, many=True)
#         return Response(serializer.data)

# class SensorList(APIView):
#     serializer_class = SensorSerializer

#     def get(self, request, format=None):
#         sensor = Sensor.objects.all()
#         serializer = ShiftSerializer(sensor, many=True)
#         return Response(serializer.data)