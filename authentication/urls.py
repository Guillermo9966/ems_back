from importlib.resources import path
from django.urls import include, path
from .views import CustomUserView, Login
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("user", CustomUserView)

urlpatterns = [   
path("", include(router.urls)),
path('login/',Login.as_view()),
#path('user', CustomUserView.as_view()),
] 