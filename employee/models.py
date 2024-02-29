from django.db import models
from django.contrib.auth.models import User


class Login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    login_time = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.email

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department= models.CharField(max_length=100)
      # Include password field here
    def __str__(self):
        return self.name