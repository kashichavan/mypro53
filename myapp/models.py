from django.db import models

# Create your models here.
class TrainerModel(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
