from django.db import models

# Create your models here.
class Arch(models.Model):
    name = models.CharField(max_length=255)
    yrbuilt = models.IntegerField()
    location = models.CharField(max_length=255)
    desc = models.CharField(max_length=4000)
    # objects = ArchManager()