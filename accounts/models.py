from django.db import models

# Create your models here.


class jobs(models.Model):
    role = models.CharField(max_length=50)
    date = models.DateField()
    location = models.CharField(max_length=100)
    count = models.IntegerField()
    duration = models.IntegerField()
    pay = models.IntegerField()
    farmer = models.CharField(max_length=100)

class taken(models.Model):
    job_id = models.IntegerField()
    date = models.DateField()
    role = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    cno = models.CharField(max_length=100)
    farmer = models.CharField(max_length=100)
