from django.db import models

# Create your models here.
class Servicios(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    precio=models.IntegerField()
    

    def __str__(self):
        return self.name
