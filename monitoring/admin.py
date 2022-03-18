from django.contrib import admin
from .models import *

admin.site.register(Company)
admin.site.register(Plant)
admin.site.register(Shift)
admin.site.register(TypeMedition)
admin.site.register(Sensor)
admin.site.register(Reading)