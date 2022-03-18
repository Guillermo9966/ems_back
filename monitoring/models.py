from django.db import models
from authentication.models import CustomUser
from rest_framework import serializers

class Company(models.Model):
    asigne_to = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=45, null=False)
    country = models.CharField(max_length=20, null=False)
    
    def __str__(self) -> str:
        return f'{self.company_name} {self.country}'
    
    
class Plant(models.Model):
    name_plant = models.CharField(max_length=30, null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name_plant
    

class Shift(models.Model):
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.start_date} {self.end_date}"
    

class TypeMedition(models.Model):
    medition_name = models.CharField(max_length=35, null=False)
    unity_type = models.CharField(max_length=5, null=False)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.medition_name} {self.unity_type}"
    
    
class Sensor(models.Model):
    sensor_name = models.CharField(max_length=10, null=False)
    type_medition = models.ForeignKey(TypeMedition, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.sensor_name
    
    
class Reading(models.Model):
    datetime = models.DateTimeField(null=False)
    value = models.FloatField(max_length=3)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.datetime} {self.value}"