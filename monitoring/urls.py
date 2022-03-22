from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from monitoring import views
from monitoring.views import  MonitoringManager, PlantList, Readinglist, SensorList, ShiftList
from monitoring.serializer import MonitoringSerializer

urlpatterns = [

    path('my-data', MonitoringManager.as_view(), name= "monitoring_list"),
    path('plant', PlantList.as_view(), name= "plant_list"),
    path('shift', ShiftList.as_view(), name= "shift_list"),
    path('sensor', SensorList.as_view(), name= "sensor_list"),
    path('reading', Readinglist.as_view(), name= "reading_list"),



    
]
urlpatterns = format_suffix_patterns(urlpatterns)