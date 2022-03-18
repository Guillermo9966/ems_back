from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import DO_NOTHING


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=125, null=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    def get_full_name_user(self):
        return {'full_name': f"{self.first_name} {self.last_name}"}
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    
    
    
    




