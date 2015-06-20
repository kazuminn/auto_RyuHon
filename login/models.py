from django.db import models

class UserFirst(models.Model):
    username = models.CharField(max_length=300,unique=False)
    password = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
