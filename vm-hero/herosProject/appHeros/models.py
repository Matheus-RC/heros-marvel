from django.db import models

# Create your models here.
class Group(models.Model):
    id_group = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Character(models.Model):
    id = models.IntegerField(primary_key=True)
    name =  models.CharField(max_length=100)
    path = models.CharField(max_length=255)
    extension = models.CharField(max_length=5)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

