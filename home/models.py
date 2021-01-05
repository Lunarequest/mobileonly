from django.db import models

# Create your models here.
class contact(models.Model):
    email=models.EmailField()
    message=models.TextField(max_length=10000)
    name=models.TextField(max_length=100)
