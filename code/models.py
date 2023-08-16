from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class ConsultationRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    project_description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
