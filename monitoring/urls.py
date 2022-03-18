from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from monitoring import views
from monitoring.views import  MonitoringManager
from monitoring.serializer import MonitoringSerializer

urlpatterns = [

    path('my-data', views.MonitoringManager.as_view(), name= "monitoring_list"),
    path('plant', views.PlantList.as_view(), name= "plant_list"),
    path('shift', views.ShiftList.as_view(), name= "shift_list"),
    path('sensor', views.SensorList.as_view(), name= "sensor_list"),


    
]
urlpatterns = format_suffix_patterns(urlpatterns)