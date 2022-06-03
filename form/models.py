 
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    DEMO_CHOICES =(
    ("Mgr", "Manager"),
    ("Emp", "Employee"),
    ("Admin", "Administrator"),
    ("Sup", "Supervisor"),
    )
      
    name = models.CharField(max_length=100)
    email = models.EmailField()
    spirit_animal = models.CharField(max_length=100)
    roles = models.CharField(max_length=100, choices = DEMO_CHOICES)
    
    
    def __str__(self):
        return self.name
      