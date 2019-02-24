from django.db import models

# Create your models here.

class ArchManager(models.Manager):
    def create_arch(self, data):
        print(data)

class Arch(models.Model):
    name = models.CharField(max_length=255)
    yrbuilt = models.IntegerField()
    location = models.CharField(max_length=255)
    desc = models.CharField(max_length=4000)
    image = models.CharField(max_length=255)

    objects = ArchManager()