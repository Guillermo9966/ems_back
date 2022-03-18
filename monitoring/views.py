from django.conf import UserSettingsHolder
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import filters
from django.shortcuts import render
import json
from django.http import Http404


from monitoring.serializer import MonitoringSerializer, PlantSerializer, SensorSerializer, ShiftSerializer
from .models import Company, Plant, Sensor, Shift
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers

from rest_framework import generics
from rest_framework import status

class MonitoringManager(APIView):
    '''
    list company 
    '''
    serializer_class = MonitoringSerializer
    def get(self, request, format=None):
        company = Company.objects.all()
        serializer = MonitoringSerializer(company, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MonitoringSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
class PlantList(APIView):
    serializer_class = PlantSerializer

    def get(self, request, format=None):
        plant = Plant.objects.all()
        serializer = PlantSerializer(plant, many=True)
        return Response(serializer.data)

class ShiftList(APIView):
    serializer_class = ShiftSerializer

    def get(self, request, format=None):
        shift = Shift.objects.all()
        serializer = ShiftSerializer(shift, many=True)
        return Response(serializer.data)

class SensorList(APIView):
    serializer_class = SensorSerializer

    def get(self, request, format=None):
        sensor = Sensor.objects.all()
        serializer = ShiftSerializer(sensor, many=True)
        return Response(serializer.data)