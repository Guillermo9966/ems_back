from rest_framework import serializers
from monitoring.models import Company, Plant, Reading, Sensor, Shift, TypeMedition
from authentication.models import CustomUser


class MonitoringSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Company
        fields = ['company_name']


class PlantSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Plant
        fields = ['company', 'name_plant']  

class ShiftSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model =Shift
        fields = '__all__'

class TypeMeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeMedition
        fields = ['medition_name', 'unity_type']       

class SensorSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Sensor
        fields = ['sensor_name', 'type_medition']  

class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ['datetime', 'value']