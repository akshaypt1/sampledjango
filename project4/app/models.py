from django.db import models

# Create your models here.
class user(models.model):
    name=models.TextField()
    email=models.TextField()
    password=models.TextField()
