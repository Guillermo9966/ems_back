from importlib.resources import path
from django.urls import include, path
from .views import Login

urlpatterns = [   
 path('login/',Login.as_view())
] 