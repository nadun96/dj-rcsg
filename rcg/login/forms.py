from django.db import models

class NewUser(models.Model):
    name = models.CharField(max_length=200)