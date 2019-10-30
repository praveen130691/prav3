from django.db import models

class Praveen(models.Model):
    user = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    mob = models.CharField(max_length=10, primary_key=True)




