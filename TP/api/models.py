from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.TextField()

    def __str__(self):
        return self.username


class Temp(models.Model):
    date = models.DateTimeField(primary_key=True)
    t_max = models.BigIntegerField()
    t_min = models.BigIntegerField()
    t_avg = models.BigIntegerField()
# Create your models here.
