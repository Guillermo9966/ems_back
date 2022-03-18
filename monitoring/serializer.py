from rest_framework import serializers
from monitoring.models import Company, Plant, Sensor, Shift
from authentication.models import CustomUser

class MonitoringSerializer(serializers.ModelSerializer):
    
    asigne_to = serializers.SerializerMethodField('get_full_name_asigne_to')
    #companie = serializers.SerializerMethodField('get_companie')   
    class Meta:
        model = Company
        fields = ['asigne_to', 'company_name']

    def get_full_name_asigne_to(self, Company):
        first_name = Company.asigne_to.first_name
        last_name = Company.asigne_to.last_name
        print(first_name)
        data = [
            {
            "first_name":first_name,
            "last_name": last_name,
            
            }
        ]
        return data

class PlantSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Plant
        fields = ['name_plant']  

class ShiftSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model =Shift
        fields = '__all__'        

class SensorSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Sensor
        fields = ['sensor_name']   