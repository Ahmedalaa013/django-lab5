from django.db import models

# Create your models here.
class Myuser(models.Model):
    Id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)