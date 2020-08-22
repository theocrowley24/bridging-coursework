from django.db import models
from django.utils import timezone

# Create your models here.

class Cv(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    emailAddress = models.CharField(max_length=100)
    aboutMe = models.TextField()

class Qualification(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="", null=False)
    startDate = models.DateField(default=timezone.now())
    endDate = models.DateField(default=timezone.now(), null=False)

class Experience(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="", null=False)
    startDate = models.DateField(default=timezone.now())
    endDate = models.DateField(default=timezone.now(), null=False)