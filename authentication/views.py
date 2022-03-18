from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import json


from .models import CustomUser
from django.contrib.auth.hashers import check_password
from rest_framework import status
from .models import *

class Login(APIView):
    def post(self, request):
        user = request.data["username"]            
        password = request.data["password"]
        user = user.replace(" ", "")

        try:
            p = CustomUser.objects.get(username=user)
            hash_pass = p.password
            verify_pass = check_password(password, hash_pass)
        except:
            data = {
                "code" : 404,
                "msg" : "User not register"
            }            
            return JsonResponse(data, status = status.HTTP_404_NOT_FOUND)
        if verify_pass:
            data = {
                "code" : 200,
                "msg" : "Login success"
            }
            return JsonResponse(data)
        elif not verify_pass:
            data = {
                "code" : 401,
                "msg" : "inicio de sesion incorrecto"
            }
            return JsonResponse(data, status = status.HTTP_401_UNAUTHORIZED)